import os
import numpy as np
import math

import pydyna

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
# custom interface
from path_following_interfaces.msg import State
#custom service
from path_following_interfaces.srv import StartEndSimul

class YawControl(Node):
    def __init__(self):
        super().__init__('yawcontrol_node')

        self.publisher_rudder = self.create_publisher(
            Float32,
            '/rudder_angle',
            1)


def main(args=None):
    rclpy.init(args=args)
    yaw_node = YawControl()

    K = 1
    
    yaw_node.get_logger().info('send yaw')

    rclpy.spin(yaw_node)

    yaw_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()