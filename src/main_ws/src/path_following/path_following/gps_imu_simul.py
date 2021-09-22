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
        
    def callback_state(self, msg):
        self.get_logger().info(
            'listened state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
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
        simulated_state = state_simul(msg)
        self.publisher_simulated_state.publish(simulated_state)
    
    def state_simul(state):
        simulated_state = State()
        simulated_state.position.x = 1 # FILLER
        simulated_state.position.y = 1 # FILLER
        simulated_state.position.psi = 1 # FILLER
        simulated_state.velocity.u = 1 # FILLER
        simulated_state.velocity.v = 1 # FILLER
        simulated_state.velocity.r = 1 # FILLER
        return simulated_state # 

def main(args=None):
    rclpy.init(args=args)
    gps_imu_simulator_node = GpsImuSimulator()
    
    rclpy.spin(gps_imu_simulator_node)

    gps_imu_simulator_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()