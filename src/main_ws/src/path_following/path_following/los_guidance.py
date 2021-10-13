import sys

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
#custom service
from path_following_interfaces.msg import Waypoints, State

class LosGuidance(Node):
    def __init__(self):
        super().__init__('los_guidance_node')

        self.des_yaw_msg = Float32()
        self.des_velocity_msg = Float32()

        self.current_waypoint = 1 #index of waypoint the ship has to reach next (includes starting (0,0,0)

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_waypoints = self.create_subscription(
            Waypoints,
            '/waypoints',
            self.callback_waypoints,
            1)

        self.subscription_filtered_state = self.create_subscription(
            State,
            '/filtered_state',
            self.callback_filtered_state,
            1)

        self.publisher_desired_yaw_angle = self.create_publisher(
            Float32,
            '/desired_yaw_angle',
            1)

        self.publisher_desired_surge_velocity = self.create_publisher(
            Float32,
            '/desired_surge_velocity',
            1)

    def log_state(self, msg):
        self.get_logger().info(
            'listened filtered state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
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

    def callback_shutdown():
        sys.exit()

    def callback_waypoints(self, msg):
        self.waypoints = msg # {position: {x: [...], y: [...]} velocity: [...]}
        num_waypoints = len(msg.position.x)
        self.get_logger().info('listened %d waypoints' % num_waypoints)
        for i in range(num_waypoints):
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, msg.position.x[i], msg.position.y[i], msg.velocity[i]))
        
    def callback_filtered_state(self, msg):
        self.log_state(msg)
        des_yaw_msg, des_velocity_msg = self.los(msg)
        self.publisher_desired_yaw_angle.publish(des_yaw_msg)
        self.get_logger().info('published desired yaw angle: %f' % des_yaw_msg.data)
        self.publisher_desired_surge_velocity.publish(des_velocity_msg)
        self.get_logger().info('published desired velocity: %f' % des_velocity_msg.data)
    
    def los(self, xf):
        # use waypoints stored in self.waypoints
        # these contain desired position x and y, and velocity u
        self.des_yaw_msg.data = 1.0
        self.des_velocity_msg.data = 1.0 
        return self.des_yaw_msg, self.des_velocity_msg

def main(args=None):
    try:
        rclpy.init(args=args)
        los_guidance_node = LosGuidance()
        rclpy.spin(los_guidance_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    finally:
        los_guidance_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()