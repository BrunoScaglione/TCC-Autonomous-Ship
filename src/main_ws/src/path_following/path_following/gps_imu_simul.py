import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class GpsImuSimulator(Node):
    def __init__(self):
        super().__init__('gps_imu_simulator_node')

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
        simulated_state_msg = self.state_simul(msg)
        self.publisher_simulated_state.publish(simulated_state_msg)
        self.log_state(simulated_state_msg, 'publisher')
    
    def state_simul(self, x):
        return x # FILLER 
    
    def log_state(self, state, communicator):
        log_str = 'listened' if communicator == 'subscriber' else 'published simulated'
        self.get_logger().info(
            '%s state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                log_str,
                state.position.x, 
                state.position.y, 
                state.position.psi, # yaw angle
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