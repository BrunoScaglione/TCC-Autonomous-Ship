import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
# custom interface
from path_following_interfaces.msg import State

class ControlAllocation(Node):
    def __init__(self):
        super().__init__('control_allocation_node')

        self.subcription_propeller_thrust = self.create_subscription(
            Float32,
            '/propeller_thrust',
            1)

        self.publisher_propeller = self.create_publisher(
            Float32,
            '/propeller_rotation',
            1)

        self.control_allocation_timer = self.create_timer(
            3.0,
            self.control_allocation_publisher
        )

    def control_allocation_publisher(self):
        propeller_rotation = 1.0
        msg = Float32()
        msg.data = propeller_rotation
        self.publisher_rudder.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    control_allocation_node = ControlAllocation()
    
    control_allocation_node.get_logger().info('send control_allocation')

    rclpy.spin(control_allocation_node)

    control_allocation_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()