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
import collections

import numpy as np

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class GpsImuSimulator(Node):
    def __init__(self):
        super().__init__('gps_imu_simulator_node')

        # params

        # GPS_rate == 10 # [Hz] 
        # IMU_rate == 2000 # [Hz]
        # both rates are faster than the simulation 
        # (10 - e Hz where e is due to the time do do 1 step of computations)
        # therefore wont have sampling effect

        # assuming sensors are already calibrated (no bias)
        # assuming same variance for x and y, and 0 covariance
        self.sigma_x = 5.46112744197 # GPS 1: from horizontal acc
        self.sigma_y = 5.46112744197 # GPS 1: from horizontal acc
        self.sigma_theta = 0.0523599 # GPS 1: from heading acc
        self.sigma_u = None # is calculated dynamically 
        self.sigma_v = None # is calculated dynamically
        self.sigma_r = 0.0005 # IMU: from bias-in-run

        self.sigma_xdot = 0.1 # GPS 2: from velocity acc
        self.sigma_ydot = 0.1 # GPS 2: from velocity acc
        
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

    def callback_shutdown():
        sys.exit()
        
    def callback_state(self, msg):
        self.log_state(msg, 'subscriber')
        self.last_two_states.appendleft(msg)
        self.calculate_velocity_sigmas()
        simulated_state_msg = self.state_simul(msg)
        self.publisher_simulated_state.publish(simulated_state_msg)
        self.log_state(simulated_state_msg, 'publisher')

    def calculate_velocity_sigmas(self):
        x_dot = ( list(self.last_two_states)[0].position.x - list(self.last_two_states)[1].position.x )/0.1
        y_dot = ( list(self.last_two_states)[0].position.y - list(self.last_two_states)[1].position.y )/0.1
        sigma_theta = self.sigma_theta
        theta = list(self.last_two_states)[0].position.theta
        # error propagation ([u, v].T = R@[xdot, ydot].T linear transformation or rotation matrix)
        self.sigma_u = ( (np.cos(theta)*self.sigma_xdot)**2 + (np.sin(theta)*self.sigma_ydot)**2 \
            + ((-np.sin(theta)*x_dot + np.cos(theta)*y_dot)*sigma_theta)**2 )**0.5
        self.sigma_v = ( (-np.sin(theta)*self.sigma_xdot)**2 + (np.cos(theta)*self.sigma_ydot)**2 \
            + ((-np.cos(theta)*x_dot - np.sin(theta)*y_dot)*sigma_theta)**2 )**0.5

    def state_simul(self, x):
        # self.xs_msg.position.x = x.position.x + np.random.normal(0, self.sigma_x) # gps
        # self.xs_msg.position.y = x.position.y + np.random.normal(0, self.sigma_y) # gps
        # self.xs_msg.position.theta = x.position.theta + np.random.normal(0, self.sigma_theta) # gyrocompass

        # self.xs_msg.velocity.u = x.velocity.u + np.random.normal(0, self.sigma_u) # gps
        # self.xs_msg.velocity.v = x.velocity.v + np.random.normal(0, self.sigma_v) # gps
        # self.xs_msg.velocity.r = x.velocity.r + np.random.normal(0, self.sigma_r) # imu

        # self.xs_msg.time = x.time

        # return self.xs_msg

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

def main(args=None):
    try:
        rclpy.init(args=args)
        gps_imu_simulator_node = GpsImuSimulator()
        rclpy.spin(gps_imu_simulator_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        gps_imu_simulator_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()