'''
Datasheets used:
    1. GPS 1: https://pdf.nauticexpo.com/pdf/san-jose-technology-inc/marine-gps-receiver/23414-76823.html
    2. GPS 2 (just for velocity): {
        https://www.u-blox.com/sites/default/files/products/documents/NEO-6_DataSheet_(GPS.G6-HW-09005).pdf or
        https://docs.rs-online.com/c0e9/0900766b80df94d1.pdf or
        https://www.generationrobots.com/media/GP-635T-121130-datasheet.pdf or
        https://4.imimg.com/data4/SO/GH/MY-23669504/gps-shield-skg13c-module.pdf
    }
    3. IMU (indutrial): https://inertiallabs.com/wp-content/uploads/2020/09/IMU-P_Datasheet.rev3_.3_Sept_2020.pdf
'''
 
import sys
import os
import glob
import traceback

import collections
import numpy as np
import matplotlib.pyplot as plt

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class GpsImuSimulator(Node):
    def __init__(self):
        super().__init__('gps_imu_simulator_node')

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value

        self.state_history = [[],[],[],[],[],[]]
        self.simulated_state_history = [[],[],[],[],[],[]]

        # GPS_rate == 10 # [Hz] 
        # IMU_rate == 2000 # [Hz]
        # both rates are faster than the simulation 
        # (which is 10-e Hz where e is due to the time do do 1 step of computations)
        # therefore wont have sampling effect

        self.TIME_STEP = 0.1

        # assuming sensors are already calibrated (no bias)
        # assuming same variance for x and y, and 0 covariance
        self.SIGMA_X = 5.46112744197 # GPS 1: from horizontal acc
        self.SIGMA_Y = 5.46112744197 # GPS 1: from horizontal acc
        self.SIGMA_THETA = 0.0523599 # GPS 1: from heading acc
        # self.sigma_u = None # is calculated dynamically 
        # self.sigma_v = None # is calculated dynamically
        self.SIGMA_R = 0.0005 # IMU: from bias-in-run

        self.SIGMA_XDOT = 0.1 # GPS 2: from velocity acc
        self.SIGMA_YDOT = 0.1 # GPS 2: from velocity acc
        
        # State() has by default all zeros
        self.last_two_states = collections.deque([State()], maxlen=2) 

        self.xs_msg = State()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_state = self.create_subscription(
            State,
            '/state',
            self.callback_state,
            1)

        self.publisher_simulated_state = self.create_publisher(
            State,
            '/simulated_state',
            1)

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
        
    def callback_state(self, msg):
        self.log_state(msg, 'subscriber')

        self.state_history[0].append(msg.position.x)
        self.state_history[1].append(msg.position.y)
        self.state_history[2].append(msg.position.theta)
        self.state_history[3].append(msg.velocity.u)
        self.state_history[4].append(msg.velocity.v)
        self.state_history[5].append(msg.velocity.r)

        self.last_two_states.appendleft(msg)
        self.calculate_velocity_sigmas()
        simulated_state_msg = self.state_simul(msg)
        self.publisher_simulated_state.publish(simulated_state_msg)
        self.log_state(simulated_state_msg, 'publisher')

    def calculate_velocity_sigmas(self):
        x_dot = ( list(self.last_two_states)[0].position.x - list(self.last_two_states)[1].position.x )/self.TIME_STEP
        y_dot = ( list(self.last_two_states)[0].position.y - list(self.last_two_states)[1].position.y )/self.TIME_STEP
        sigma_theta = self.SIGMA_THETA
        theta = list(self.last_two_states)[0].position.theta
        # error propagation ([u, v].T = R@[xdot, ydot].T linear transformation or rotation matrix)
        self.sigma_u = ( (np.cos(theta)*self.SIGMA_XDOT)**2 + (np.sin(theta)*self.SIGMA_YDOT)**2 \
            + ((-np.sin(theta)*x_dot + np.cos(theta)*y_dot)*sigma_theta)**2 )**0.5
        self.sigma_v = ( (-np.sin(theta)*self.SIGMA_XDOT)**2 + (np.cos(theta)*self.SIGMA_YDOT)**2 \
            + ((-np.cos(theta)*x_dot - np.sin(theta)*y_dot)*sigma_theta)**2 )**0.5

    def state_simul(self, x):
        # self.xs_msg.position.x = x.position.x + np.random.normal(0, self.SIGMA_X) # gps
        # self.xs_msg.position.y = x.position.y + np.random.normal(0, self.SIGMA_Y) # gps
        # self.xs_msg.position.theta = x.position.theta + np.random.normal(0, self.SIGMA_THETA) # gyrocompass

        # self.xs_msg.velocity.u = x.velocity.u + np.random.normal(0, self.sigma_u) # gps
        # self.xs_msg.velocity.v = x.velocity.v + np.random.normal(0, self.sigma_v) # gps
        # self.xs_msg.velocity.r = x.velocity.r + np.random.normal(0, self.SIGMA_R) # imu

        # self.xs_msg.time = x.time

        # return self.xs_msg

        # must change x for xs_msg when this node is functioning
        self.simulated_state_history[0].append(x.position.x)
        self.simulated_state_history[1].append(x.position.y)
        self.simulated_state_history[2].append(x.position.theta)
        self.simulated_state_history[3].append(x.velocity.u)
        self.simulated_state_history[4].append(x.velocity.v)
        self.simulated_state_history[5].append(x.velocity.r)

        return x # debugging wave filter

    def log_state(self, state, communicator):
        log_str = 'listened' if communicator == 'subscriber' else 'published simulated'
        self.get_logger().info(
            '%s state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                log_str,
                state.position.x, 
                state.position.y, 
                state.position.theta, # yaw angle
                state.velocity.u, 
                state.velocity.v, 
                state.velocity.r,
                state.time 
            )
        )

    def generate_plots(self):
        # clean before
        files = glob.glob(os.path.join(self.plots_dir, 'simulatedState', '*.png'))
        for f in files:
            os.remove(f)
        files = glob.glob(os.path.join(self.plots_dir, 'state', '*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = [self.TIME_STEP*i for i in range(len(self.simulated_state_history[0]))]
        ss_dir = "simulatedState"
        simulated_state_props = [
            {
                "title": "Simulated Linear Position X",
                "ylabel": "x [m]",
                "file": "simulatedLinearPositionX.png"
            },
            {
                "title": "Simulated Linear Position Y",
                "ylabel": "y [m]",
                "file": "simulatedLinearPositionY.png"
            },
            {
                "title": "Simulated Angular Position Theta",
                "ylabel": r"$\theta\;[rad\;(from\;east\;counterclockwise)]$",
                "file": "simulatedAngularPositionTheta.png"
            },
            {
                "title": "Simulated Linear Velocity U",
                "ylabel": "u [m/s]",
                "file": "simulatedLinearVelocityU.png"
            },
            {
                "title": "Simulated Linear Position V",
                "ylabel": "v [m/s (port)]",
                "file": "simulatedLinearVelocityV.png"
            },
            {
                "title": "Simulated Angular Velocity R",
                "ylabel": "r [rad/s (counterclockwise)]",
                "file": "simulatedAngularVelocityR.png"
            },
        ]
        s_dir = "state"
        state_props = [
            {
                "title": "Linear Position X",
                "ylabel": "x [m]",
                "file": "linearPositionX.png"
            },
            {
                "title": "Linear Position Y",
                "ylabel": "$y [m]",
                "file": "linearPositionY.png"
            },
            {
                "title": "Angular Position Theta",
                "ylabel": r"$\theta\;[rad\;(from\;east\;counterclockwise)]$",
                "file": "angularPositionTheta.png"
            },
            {
                "title": "Linear Velocity U",
                "ylabel": "$u [m/s]",
                "file": "linearVelocityU.png"
            },
            {
                "title": "Linear Position V",
                "ylabel": "$v [m/s\;(port)]",
                "file": "linearVelocityV.png"
            },
            {
                "title": "Angular Velocity R",
                "ylabel": "r [rad/s (counterclockwise)]",
                "file": "angularVelocityR.png"
            },
        ]
        dirs = [ss_dir, s_dir]
        propss = [simulated_state_props, state_props]
        histories = [self.simulated_state_history, self.state_history]
        for (dir, props, history) in list(zip(dirs, propss, histories)):
            for j in range(len(history)):
                fig, ax = plt.subplots(1)
                ax.set_title(props[j]["title"])
                ax.plot(t, history[j])
                ax.set_xlabel("t [s]")
                ax.set_ylabel(props[j]["ylabel"])
                ax.set_ylim([min(history[j]), max(history[j])])

                fig.savefig(os.path.join(self.plots_dir, dir, props[j]["file"]))

def main(args=None):
    try:
        rclpy.init(args=args)
        gps_imu_simulator_node = GpsImuSimulator()
        rclpy.spin(gps_imu_simulator_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        gps_imu_simulator_node.generate_plots()
        gps_imu_simulator_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()