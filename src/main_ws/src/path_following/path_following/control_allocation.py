import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
# custom interface
from path_following_interfaces.msg import State

class ControlAllocation(Node):
    def __init__(self):
        super().__init__('control_allocation_node')

        self.subscription_propeller_thrust = self.create_subscription(
            Float32,
            '/propeller_thrust',
            self.callback_propeller_thrust,
            1)

        self.publisher_propeller_rotation = self.create_publisher(
            Float32,
            '/propeller_rotation',
            1)
        
    def callback_propeller_thrust(self, msg):
        self.get_logger().info('listened propeller thrust: %f' % msg.data)
        propeller_rotation = self.control_allocation(msg.data)
        self.publisher_propeller_rotation.publish(propeller_rotation)
    
    def control_allocation(self, propeller_thrust):
        rotation_msg = Float32()
        rotation_msg.data = 1 # FILLER [hZ]
        return rotation_msg # 

def main(args=None):
    rclpy.init(args=args)
    control_allocation_node = ControlAllocation()
    
    rclpy.spin(control_allocation_node)

    control_allocation_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()