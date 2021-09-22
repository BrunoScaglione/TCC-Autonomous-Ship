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
        
    def callback_simulated_state(self, msg):
        self.get_logger().info(
            'listened simulated state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                msg.position.x, 
                msg.position.y, 
                msg.position.psi, # yaw angle
                msg.velocity.u, 
                msg.velocity.v, 
                msg.velocity.r,
                msg.time 
            )
        )
        estimated_state = state_estimate(msg)
        self.publisher_estimated_state.publish(estimated_state)
    
    def state_estimate(state_simul):
        estimated_state = State()
        estimated_state.position.x = 1 # FILLER
        estimated_state.position.y = 1 # FILLER
        estimated_state.position.psi = 1 # FILLER
        estimated_state.velocity.u = 1 # FILLER
        estimated_state.velocity.v = 1 # FILLER
        estimated_state.velocity.r = 1 # FILLER
        return estimated_state # 

def main(args=None):
    rclpy.init(args=args)
    kalman_filter_node = KalmanFIlter()
    
    rclpy.spin(kalman_filter_node)

    kalman_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()