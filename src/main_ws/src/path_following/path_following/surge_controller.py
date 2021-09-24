import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class SurgeController(Node):
    def __init__(self):
        super().__init__('surge_controller_node')

        self.desired_surge_velocity = 0

        self.thrust_msg = Float32()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_filtered_state = self.create_subscription(
            State,
            '/filtered_state',
            self.callback_filtered_state,
            1)

        self.subscription_desired_surge_velocity = self.create_subscription(
            Float32,
            '/desired_surge_velocity',
            self.callback_desired_surge_velocity,
            1)

        self.publisher_propeller_thrust = self.create_publisher(
            Float32,
            '/propeller_thrust',
            1)

    def callback_shutdown():
        sys.exit()
        
    def callback_filtered_state(self, msg):
        self.get_logger().info('listened filtered surge velocity: %f' % msg.velocity.u)
        thrust_msg = self.surge_control(msg.velocity.u)
        self.publisher_propeller_thrust.publish(thrust_msg)
        self.get_logger().info('published thrust force: %f' % thrust_msg.data)
    
    def callback_desired_surge_velocity(self, msg):
        self.get_logger().info('listened desired surge velocity: %f' % msg.data)
        self.desired_surge_velocity = msg.data
    
    def surge_control(self, u): # u is surge velocity
        u_des = self.desired_surge_velocity
        self.thrust_msg.data = 1.0 
        return self.thrust_msg 

def main(args=None):
    try:
        rclpy.init(args=args)
        surge_controller_node = SurgeController()
        rclpy.spin(surge_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        surge_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()