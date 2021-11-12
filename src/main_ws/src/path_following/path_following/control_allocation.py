import sys
import math

import matplotlib as plt #debugging

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
from std_msgs.msg import Float32

# custom iterfaces
from path_following_interfaces.msg import State

class ControlAllocation(Node):
    def __init__(self):
        super().__init__('control_allocation_node')

        # controller parameters
        self.C1 = 0.036
        self.C2 = 3.53
        self.C3 = 0.06696

        self.PROPELLER_SAT = 1.75 # Hz

        self.propeller_history = [] #debugging

        self.rotation_msg = Float32()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_estimated_state = self.create_subscription(
            State,
            '/estimated_state',
            self.callback_estimated_state,
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
    
    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()

    def callback_estimated_state(self, msg):
        self.get_logger().info('listened estimated surge velocity: %f' % msg.velocity.u)
        self.surge_velocity = msg.velocity.u
        
    def callback_propeller_thrust(self, msg):
        self.get_logger().info('listened propeller thrust: %f' % msg.data)
        propeller_rotation_msg = self.control_allocation(msg.data, self.surge_velocity)
        self.publisher_propeller_rotation.publish(propeller_rotation_msg)
        self.get_logger().info('published propeller rotation: %f' % propeller_rotation_msg.data)
    
    def control_allocation(self, tau, u):
        if tau > 0:
            Np = self.C1*(math.sqrt(self.C2*(u**2) + tau)) + self.C3*u
        else:
            Np = -(self.C1*(math.sqrt(self.C2*(u**2) - tau)) + self.C3*u)
        # saturation of the propeller (with 1% safety margin)
        # real sat is 1.75 Hz
        Np = max(-self.PROPELLER_SAT*0.99, min(Np, self.PROPELLER_SAT*0.99))
        self.propeller_history.append(Np)
        self.rotation_msg.data = Np
        return self.rotation_msg 

def main(args=None):
    try:
        rclpy.init(args=args)
        control_allocation_node = ControlAllocation()
        rclpy.spin(control_allocation_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        # debugging
        plt.plot(control_allocation_node.propeller_history)
        plt.show()
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        control_allocation_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()