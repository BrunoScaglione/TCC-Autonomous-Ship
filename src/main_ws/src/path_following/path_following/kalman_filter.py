import rclpy
from rclpy.node import Node

# custom interface
from path_following_interfaces.msg import State

class KalmanFilter(Node):
    def __init__(self):
        super().__init__('kalman_filter_simulator_node')

        self.subscription_simulated_state = self.create_subscription(
            State,
            '/simulated_state',
            self.callback_simulated_state,
            1)

        self.publisher_estimated_state = self.create_publisher(
            State,
            '/estimated_state',
            1)

    def log_state(self, msg, communicator):
        log_str = 'listened simulated' if communicator == 'subscriber' else 'published estimated'
        self.get_logger().info(
            '%s state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                log_str,
                msg.state.position.x, 
                msg.state.position.y, 
                msg.state.position.psi, # yaw angle
                msg.state.velocity.u, 
                msg.state.velocity.v, 
                msg.state.velocity.r,
                msg.state.time 
            )
        )
        
    def callback_simulated_state(self, msg):
        log_state(self, msg, 'subscriber')
        estimated_state_msg = self.state_estimate(msg)
        self.publisher_estimated_state.publish(estimated_state_msg)
        log_state(self, estimated_state_msg, 'publisher')

    
    def state_estimate(xs):
        xe_msg = State()
        xe_msg.position.x = 1 # FILLER
        xe_msg.position.y = 1 # FILLER
        xe_msg.position.psi = 1 # FILLER
        xe_msg.velocity.u = 1 # FILLER
        xe_msg.velocity.v = 1 # FILLER
        xe_msg.velocity.r = 1 # FILLER
        return xe_msg # 

def main(args=None):
    rclpy.init(args=args)
    kalman_filter_node = KalmanFIlter()
    
    rclpy.spin(kalman_filter_node)

    kalman_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()