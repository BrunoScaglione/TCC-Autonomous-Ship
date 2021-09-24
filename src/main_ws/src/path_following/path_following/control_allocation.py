import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from std_msgs.msg import Float32

class ControlAllocation(Node):
    def __init__(self):
        super().__init__('control_allocation_node')

        self.rotation_msg = Float32()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_propeller_thrust = self.create_subscription(
            Float32,
            '/propeller_thrust',
            self.callback_propeller_thrust,
            1)

        self.publisher_propeller_rotation = self.create_publisher(
            Float32,
            '/propeller_rotation',
            1)
    
    def callback_shutdown():
        sys.exit()
        
    def callback_propeller_thrust(self, msg):
        self.get_logger().info('listened propeller thrust: %f' % msg.data)
        propeller_rotation = self.control_allocation(msg.data)
        self.publisher_propeller_rotation.publish(propeller_rotation)
    
    def control_allocation(self, tau):
        self.rotation_msg.data = 1.0
        return self.rotation_msg 

def main(args=None):
    try:
        rclpy.init(args=args)
        control_allocation_node = ControlAllocation()
        rclpy.spin(control_allocation_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        control_allocation_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()