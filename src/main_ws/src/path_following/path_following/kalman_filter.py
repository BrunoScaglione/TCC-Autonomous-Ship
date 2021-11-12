import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class KalmanFilter(Node):
    def __init__(self):
        super().__init__('kalman_filter_simulator_node')

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

    def state_estimate(self, xs):
        return xs # FILLER

def main(args=None):
    try:
        rclpy.init(args=args)
        kalman_filter_node = KalmanFilter()
        rclpy.spin(kalman_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        kalman_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()