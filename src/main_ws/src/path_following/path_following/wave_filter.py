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
        
    def callback_estimated_state(self, msg):
        self.get_logger().info(
            'listened estimated state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
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
        filtered_state = state_filter(msg)
        self.publisher_filtered_state.publish(filtered_state)
    
    def state_filter(state_estimate):
        filtered_state = State()
        filtered_state.position.x = 1 # FILLER
        filtered_state.position.y = 1 # FILLER
        filtered_state.position.psi = 1 # FILLER
        filtered_state.velocity.u = 1 # FILLER
        filtered_state.velocity.v = 1 # FILLER
        filtered_state.velocity.r = 1 # FILLER
        return filtered_state # 

def main(args=None):
    rclpy.init(args=args)
    wave_filter_node = WaveFilter()
    
    rclpy.spin(wave_filter_node)

    wave_filter_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()