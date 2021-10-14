import sys

import numpy as np
from scipy.optimize import fsolve

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
#custom service
from path_following_interfaces.msg import Waypoints, State

class LosGuidance(Node):
    def __init__(self):
        super().__init__('los_guidance_node')

        # los parameters
        self.R = 186*2 # leght*2, hardcoded for our ship

        self.des_yaw_msg = Float32()
        self.des_velocity_msg = Float32()

        #index of waypoint the ship has to reach next (first waypoint is starting position)
        self.current_waypoint = 1 

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
        msg.position.x.insert(0, 0)
        msg.position.y.insert(0, 0)
        msg.velocity.insert(0, 0) # FILLER (just to maintain same lenght of the lists)
        self.waypoints = msg # {position: {x: [...], y: [...]} velocity: [...]}
        
        num_waypoints = len(msg.position.x)
        self.get_logger().info('initial waypoint + listened %d waypoints' % (num_waypoints-1))
        for i in range(num_waypoints):
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, msg.position.x[i], msg.position.y[i], msg.velocity[i]))
        
    def callback_filtered_state(self, msg):
        self.log_state(msg)
        des_yaw_msg, des_velocity_msg = self.los(msg)
        self.publisher_desired_yaw_angle.publish(des_yaw_msg)
        self.get_logger().info('published desired yaw angle: %f' % des_yaw_msg.data)
        self.publisher_desired_surge_velocity.publish(des_velocity_msg)
        self.get_logger().info('published desired velocity: %f' % des_velocity_msg.data)
    
        
    def reached_next_waypoint(self, xf):
        x, y = xf.position.x, xf.position.y
        idx = self.current_waypoint
        wx, wy = self.waypoints.position.x[idx], self.waypoints.position.y[idx]
        return 1 if (x-wx)**2 + (y-wy)**2 < self.R**2 else 0

    @staticmethod
    def equations(p, params):
        x_los, y_los = p
        wx, wy, wx_past, wy_past, R = params
        return (
            (x_los-wx)**2 + (y_los-wy)**2 - R**2, 
            ((wy - wy_past)/(wx - wx_past))*(x_los - wx) - (y_los - wy)
        )
    
    def los(self, xf):
        # use waypoints stored in self.waypoints
        # these contain desired position x and y, and velocity u
        num_waypoints = len(self.waypoints.position.x)
        if self.reached_next_waypoint(xf) and self.current_waypoint < num_waypoints-1:
            self.current_waypoint += 1

            idx = self.current_waypoint
            x, y = xf.position.x, xf.position.y
            u, v = xf.velocity.u, xf.velocity.v
            U = (u**2  + v**2)**0.5
            wx, wy = self.waypoints.position.x[idx], self.waypoints.position.y[idx]
            wx_past, wy_past = self.waypoints.position.x[idx-1], self.waypoints.position.y[idx-1]

            # find x_los and y_los by solving 2 eq
            # analytic solution:
            # 1. isolating x_los
            # ((wy - wy_past)/(wx - wx_past))*(x_los - wx) == (y_los - wy)
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))
            # 2.  substitute and solve for y_los
            # (x_los-wx)**2 + (y_los-wy)**2 == self.R**2
            # 3.  get x_los
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))

            x_los, y_los = fsolve(self.equations, (1, 1), args=(wx, wy, wx_past, wy_past, self.R))
            beta = np.arcsin(v/U)
            chi_d = np.arctan2((y_los - y)/(x_los - x))
            psi_d =  chi_d - beta

            self.des_yaw_msg.data = psi_d
            self.des_velocity_msg.data = u
            return self.des_yaw_msg, self.des_velocity_msg
        elif self.current_waypoint == num_waypoints-1:
            self.get_logger().info('Reached final waypoint Uhulll')

            self.des_yaw_msg.data = 0
            self.des_velocity_msg.data = 0
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