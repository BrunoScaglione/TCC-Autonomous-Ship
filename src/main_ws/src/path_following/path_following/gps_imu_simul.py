import rclpy
from rclpy.node import Node

# custom interface
from path_following_interfaces.msg import State

class GpsImuSimulator(Node):
    def __init__(self):
        super().__init__('gps_imu_simulator_node')

        self.subscription_state = self.create_subscription(
            State,
            '/state',
            self.callback_state,
            1)

        self.publisher_simulated_state = self.create_publisher(
            State,
            '/simulated_state',
            1)

    def log_state(self, msg, communicator):
        log_str = 'listened' if communicator == 'subscriber' else 'published simulated'
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
        
    def callback_state(self, msg):
        log_state(self, msg, 'subscriber')
        simulated_state_msg = state_simul(msg)
        self.publisher_simulated_state.publish(simulated_state_msg)
        log_state(self, msg, 'publisher')
    
    def state_simul(state):
        simulated_state_msg = State()
        simulated_state_msg.position.x = 1 # FILLER
        simulated_state_msg.position.y = 1 # FILLER
        simulated_state_msg.position.psi = 1 # FILLER
        simulated_state_msg.velocity.u = 1 # FILLER
        simulated_state_msg.velocity.v = 1 # FILLER
        simulated_state_msg.velocity.r = 1 # FILLER
        return simulated_state_msg # 

def main(args=None):
    rclpy.init(args=args)
    gps_imu_simulator_node = GpsImuSimulator()
    
    rclpy.spin(gps_imu_simulator_node)

    gps_imu_simulator_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()