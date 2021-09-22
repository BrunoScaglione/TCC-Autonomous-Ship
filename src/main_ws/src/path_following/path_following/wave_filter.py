import rclpy
from rclpy.node import Node

# custom interface
from path_following_interfaces.msg import State

class WaveFilter(Node):
    def __init__(self):
        super().__init__('wave_filter_node')

        self.subscription_estimated_state = self.create_subscription(
            State,
            '/estimated_state',
            self.callback_estimated_state,
            1)

        self.publisher_filtered_state = self.create_publisher(
            State,
            '/filtered_state',
            1)

    def log_state(self, msg, communicator):
        log_str = 'listened estimated' if communicator == 'subscriber' else 'published filtered'
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
        
    def callback_estimated_state(self, msg):
        log_state(self, msg, 'subscriber')
        filtered_state_msg = self.state_filter(msg)
        self.publisher_filtered_state.publish(filtered_state_msg)
        log_state(self, msg, 'publisher')
    
    def state_filter(state_estimate):
        filtered_state_msg = State()
        filtered_state_msg.position.x = 1 # FILLER
        filtered_state_msg.position.y = 1 # FILLER
        filtered_state_msg.position.psi = 1 # FILLER
        filtered_state_msg.velocity.u = 1 # FILLER
        filtered_state_msg.velocity.v = 1 # FILLER
        filtered_state_msg.velocity.r = 1 # FILLER
        return filtered_state_msg # 

def main(args=None):
    rclpy.init(args=args)
    wave_filter_node = WaveFilter()
    
    rclpy.spin(wave_filter_node)

    wave_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()