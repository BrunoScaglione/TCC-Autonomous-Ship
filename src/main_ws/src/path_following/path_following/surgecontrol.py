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

class SurgeControl(Node):
    def __init__(self):
        super().__init__('surgecontrol_node')

        self.publisher_propeller = self.create_publisher(
            Float32,
            '/propeller_rotation',
            1)


def main(args=None):

    K = 1

    rclpy.init(args=args)
    surge_node = SurgeControl()
    
    surge_node.get_logger().info('send yaw')

    rclpy.spin(surge_node)

    surge_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()