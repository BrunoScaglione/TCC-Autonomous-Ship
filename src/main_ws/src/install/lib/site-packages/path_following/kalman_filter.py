import rclpy
from rclpy.node import Node

# custom interface
from path_following_interfaces.msg import State

class KalmanFilter(Node):
    def __init__(self):
        super().__init__('kalman_filter_simulator_node')

        self.xe_msg = State()

        self.subscription_simulated_state = self.create_subscription(
            State,
            '/simulated_state',
            self.callback_simulated_state,
            1)

        self.publisher_estimated_state = self.create_publisher(
            State,
            '/estimated_state',
            1)
        
    def callback_simulated_state(self, msg):
        self.log_state(msg, 'subscriber')
        estimated_state_msg = self.state_estimate(msg)
        self.publisher_estimated_state.publish(estimated_state_msg)
        self.log_state(estimated_state_msg, 'publisher')
    
    def log_state(self, state, communicator):
        log_str = 'listened simulated' if communicator == 'subscriber' else 'published estimated'
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

    def state_estimate(self, xs):
        self.xe_msg.position.x = 1.0 # FILLER
        self.xe_msg.position.y = 1.0 # FILLER
        self.xe_msg.position.psi = 1.0 # FILLER
        self.xe_msg.velocity.u = 1.0 # FILLER
        self.xe_msg.velocity.v = 1.0 # FILLER
        self.xe_msg.velocity.r = 1.0 # FILLER
        return self.xe_msg # 

def main(args=None):
    try:
        rclpy.init(args=args)
        kalman_filter_node = KalmanFilter()
        rclpy.spin(kalman_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    finally:
        kalman_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()