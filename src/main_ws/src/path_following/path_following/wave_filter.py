import rclpy
from rclpy.node import Node

# custom interface
from path_following_interfaces.msg import State

class WaveFilter(Node):
    def __init__(self):
        super().__init__('wave_filter_node')

        self.xf_msg = State()

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
        self.log_state(msg, 'subscriber')
        filtered_state_msg = self.state_filter(msg)
        self.publisher_filtered_state.publish(filtered_state_msg)
        self.log_state(filtered_state_msg, 'publisher')
    
    def state_filter(self, x):
        self.xf_msg.position.x = 1.0 # FILLER
        self.xf_msg.position.y = 1.0 # FILLER
        self.xf_msg.position.psi = 1.0 # FILLER
        self.xf_msg.velocity.u = 1.0 # FILLER
        self.xf_msg.velocity.v = 1.0 # FILLER
        self.xf_msg.velocity.r = 1.0 # FILLER
        return self.xf_msg # 

    def log_state(self, state, communicator):
        log_str = 'listened estimated' if communicator == 'subscriber' else 'published filtered'
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
        wave_filter_node = WaveFilter()
        rclpy.spin(wave_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    finally:
        wave_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()