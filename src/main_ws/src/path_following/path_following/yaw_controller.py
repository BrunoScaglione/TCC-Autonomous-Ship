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

        self.rudder_sat = 0.610865

        # desired yaw angle
        # TODO: it is hardcoded now, this would need to be set according
        #  to waypoints and inital conditions actually, use a fucntion to set
        # this value
        self.desired_yaw_angle = 1.334889326 # radians

        self.desired_yaw_angle_old = 0

        # for the integral action (acumulates error)
        self.theta_bar_int = 0

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
        self.get_logger().info('listened filtered yaw angle: %f' % msg.position.theta)
        rudder_msg = self.yaw_control(msg.position.theta, msg.velocity.r)
        self.publisher_rudder_angle.publish(rudder_msg)
        self.get_logger().info('published rudder angle: %f' % rudder_msg.data)
    
    def callback_desired_yaw_angle(self, msg):
        self.get_logger().info('listened desired yaw angle: %f' % msg.data)
        self.desired_yaw_angle_old = self.desired_yaw_angle
        self.desired_yaw_angle = msg.data
    
    def yaw_control(self, theta, r):
        # desired theta
        theta_des = self.desired_yaw_angle
        # last desired theta
        theta_des_old = self.desired_yaw_angle_old
        # error
        theta_bar = theta - theta_des
        # derivative of the error (derivative action)
        theta_bar_dot = r - (theta_des - theta_des_old)/0.1
        # cumulative of the error (integral action)
        self.theta_bar_int = self.theta_bar_int + theta_bar*0.1
        # anti windup for the integral action
        self.theta_bar_int = max(-0.5,min(self.theta_bar_int,0.5))

        # control action 
        rudder_angle = -self.Kp * theta_bar - self.Kd - theta_bar_dot - self.Ki * self.theta_bar_int
        # rudder saturation
        rudder_angle = max(-self.rudder_sat, min(rudder_angle, self.rudder_sat))
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