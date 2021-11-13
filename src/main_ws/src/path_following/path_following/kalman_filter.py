import sys
import os
import glob

import traceback

import matplotlib.pyplot as plt

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class KalmanFilter(Node):
    def __init__(self):
        super().__init__('kalman_filter_simulator_node')

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value

        self.TIME_STEP = 0.1

        self.estimated_state_history = [[],[],[],[],[],[]]

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_filtered_state = self.create_subscription(
            State,
            '/filtered_state',
            self.callback_filtered_state,
            1)

        self.publisher_estimated_state = self.create_publisher(
            State,
            '/estimated_state',
            1)

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
        
    def callback_filtered_state(self, msg):
        self.log_state(msg, 'subscriber')
        estimated_state_msg = self.state_estimate(msg)
        self.publisher_estimated_state.publish(estimated_state_msg)
        self.log_state(estimated_state_msg, 'publisher')

    def state_estimate(self, xs):

        # must change xs for xe_msg when this node is functioning
        self.estimated_state_history[0].append(xs.position.x)
        self.estimated_state_history[1].append(xs.position.y)
        self.estimated_state_history[2].append(xs.position.theta)
        self.estimated_state_history[3].append(xs.velocity.u)
        self.estimated_state_history[4].append(xs.velocity.v)
        self.estimated_state_history[5].append(xs.velocity.r)

        return xs # FILLER

    def log_state(self, state, communicator):
        log_str = 'listened filtered' if communicator == 'subscriber' else 'published estimated'
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
        #clean before
        files = glob.glob(os.path.join(self.plots_dir, 'estimatedState', '*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = [self.TIME_STEP*i for i in range(len(self.estimated_state_history[0]))]
        es_dir = "estimatedState"
        estimated_state_props = [
            {
                "title": "Estimated Linear Position X",
                "ylabel": r"$x\;[m]$",
                "file": "estimatedLinearPositionX.png"
            },
            {
                "title": "Estimated Linear Position Y",
                "ylabel": r"$y\;[m]$",
                "file": "estimatedLinearPositionY.png"
            },
            {
                "title": "Estimated Angular Position Theta",
                "ylabel": r"$\theta\;[rad\;(from\;east\;counterclockwise)]$",
                "file": "estimatedAngularPositionTheta.png"
            },
            {
                "title": "Estimated Linear Velocity U",
                "ylabel": r"$u\;[m/s]$",
                "file": "estimatedLinearVelocityU.png"
            },
            {
                "title": "Estimated Linear Position V",
                "ylabel": r"$v\;[m/s\;(port)]$",
                "file": "estimatedLinearVelocityV.png"
            },
            {
                "title": "Estimated Angular Velocity R",
                "ylabel": r"$r\;[rad/s\;(counterclockwise)]$",
                "file": "estimatedAngularVelocityR.png"
            },
        ]

        for i in range(len(self.estimated_state_history)):
            fig, ax = plt.subplots(1)
            ax.set_title(estimated_state_props[i]["title"])
            ax.plot(t, self.estimated_state_history[i])
            ax.set_xlabel(r"$t\;[s]$")
            ax.set_ylabel(estimated_state_props[i]["ylabel"])
            ax.set_ylim([min(self.estimated_state_history[i]), max(self.estimated_state_history[i])])

            fig.savefig(os.path.join(self.plots_dir, es_dir, estimated_state_props[i]["file"]))

def main(args=None):
    try:
        rclpy.init(args=args)
        kalman_filter_node = KalmanFilter()
        rclpy.spin(kalman_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        kalman_filter_node.generate_plots()
        kalman_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()