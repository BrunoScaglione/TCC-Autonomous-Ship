import sys
import math

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class YawController(Node):
    def __init__(self):
        super().__init__('yaw_controller_node')

        #parameters
        self.Kp = 1.34
        self.Kd = 49.684
        self.Ki = 0.00583

        self.counter = 0.0
        self.temp = 0.0
        self.rd = 0.0
        self.initial = 0.0

        self.desired_yaw_angle = 0

        self.rudder_msg = Float32()

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

        self.subscription_desired_yaw_angle = self.create_subscription(
            Float32,
            '/desired_yaw_angle',
            self.callback_desired_yaw_angle,
            1)

        self.publisher_rudder_angle = self.create_publisher(
            Float32,
            '/rudder_angle',
            1)

    def callback_shutdown():
        sys.exit()
        
    def callback_filtered_state(self, msg):
        self.get_logger().info('listened filtered yaw angle: %f' % msg.position.psi)
        rudder_msg = self.yaw_control(msg.position.psi, msg.velocity.r)
        self.publisher_rudder_angle.publish(rudder_msg)
        self.get_logger().info('published rudder angle: %f' % rudder_msg.data)
    
    def callback_desired_yaw_angle(self, msg):
        self.get_logger().info('listened desired yaw angle: %f' % msg.data)
        self.desired_yaw_angle = msg.data
    
    def yaw_control(self, psi, r):
        # psi desejado
        psi_des = self.desired_yaw_angle
        psi_des = math.radians(0)

        if self.rd == 0.0 and self.initial == 0:
            self.rd = psi_des
            self.temp = psi_des
            self.initial = 1
        else:
            self.rd = (psi_des - self.temp)/0.1
            self.temp = psi_des

        # psi ~ = psi_bar
        psi_bar = psi - psi_des

        #rudder_angle
        rudder_angle = - self.Kp * psi_bar - self.Kd * (r -self.rd) - self.Ki * self.counter


        if rudder_angle > 0.6108:
            rudder_angle = 0.6108
        
        if rudder_angle < -0.6108:
            rudder_angle = -0.6108

        self.counter = self.counter + (psi_bar * 0.1)
    
        if self.counter > 0.5:
            self.counter = 0.5
        
        if self.counter < -0.5:
            self.counter = -0.5

        self.rudder_msg.data = rudder_angle
        return self.rudder_msg 

def main(args=None):
    try:
        rclpy.init(args=args)
        yaw_controller_node = YawController()
        rclpy.spin(yaw_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        yaw_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()