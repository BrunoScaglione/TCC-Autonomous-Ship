import sys

import math
from sympy import symbols, Eq, solve
# import stackprinter

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

        # index of waypoint the ship has to reach next (first waypoint is starting position)
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
            'listened filtered state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                msg.position.x, 
                msg.position.y, 
                msg.position.theta, # yaw angle
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
        try: # need have received waypoints first
            self.log_state(msg)
            des_yaw_msg, des_velocity_msg = self.los(msg)
            self.publisher_desired_yaw_angle.publish(des_yaw_msg)
            self.get_logger().info('published desired yaw angle: %f' % des_yaw_msg.data)
            self.publisher_desired_surge_velocity.publish(des_velocity_msg)
            self.get_logger().info('published desired velocity: %f' % des_velocity_msg.data)
        except AttributeError:
            self.get_logger().info('Has not received waypoints yet, will ignore listened state')
        
    def reached_next_waypoint(self, xf):
        x, y = xf.position.x, xf.position.y
        idx = self.current_waypoint
        wx_next , wy_next  = self.waypoints.position.x[idx], self.waypoints.position.y[idx]
        return 1 if (x-wx_next)**2 + (y-wy_next)**2 < self.R**2 else 0

    def solve_system_of_equations(self, x, y, wx_next, wy_next, wx, wy):
        x_los, y_los = symbols('x_los, y_los')
        eq1 = Eq((x_los-x)**2 + (y_los-y)**2, self.R**2)
        eq2 = Eq(((wy_next - wy)/(wx_next - wx)), (y_los - wy)/(x_los - wx))

        sol = solve([eq1, eq2], [x_los, y_los])
        soln = [tuple(v.evalf() for v in s) for s in sol] # evaluated numerically

        # choose right solution (closest to next waypoint)
        x_los1, y_los1 = soln[0]
        x_distance1 = abs(wx_next - x_los1)
        x_los2, y_los2 = soln[1]
        x_distance2 = abs(wx_next - x_los2)

        #debugging
        self.get_logger().info('wx_next: %f' % wx_next)

        if x_distance1 < x_distance2:
            self.get_logger().info('x_los: %f, y_los: %f' % (x_los1, y_los1))
        else:
            self.get_logger().info('x_los: %f, y_los: %f' % (x_los2, y_los2))

        return (x_los1, y_los1) if x_distance1 < x_distance2 else (x_los2, y_los2)
    
    def los(self, xf):
        # use waypoints stored in self.waypoints
        # these contain desired position x and y, and velocity u
        num_waypoints = len(self.waypoints.position.x)
        self.get_logger().info('num_waypoints: %d' % num_waypoints)

        if self.reached_next_waypoint(xf):
            self.current_waypoint += 1
            self.get_logger().info('changed waypoint at time: %f' % xf.time)

        if self.current_waypoint < num_waypoints:
            idx = self.current_waypoint
            x, y = xf.position.x, xf.position.y
            u, v = xf.velocity.u, xf.velocity.v
            U = (u**2 + v**2)**0.5
            wx_next, wy_next, wv_next = self.waypoints.position.x[idx], self.waypoints.position.y[idx], self.waypoints.velocity[idx]
            wx, wy = self.waypoints.position.x[idx-1], self.waypoints.position.y[idx-1]

            # find x_los and y_los by solving 2 eq
            # analytic solution:
            # 1. isolating x_los
            # ((wy - wy_past)/(wx - wx_past))*(x_los - wx) == (y_los - wy)
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))
            # 2.  substitute and solve for y_los
            # (x_los-wx)**2 + (y_los-wy)**2 == self.R**2
            # 3.  get x_los
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))

            x_los, y_los = self.solve_system_of_equations(x, y, wx_next, wy_next, wx, wy)
            beta = math.asin(v/U)
            chi_d = math.atan2(x_los - x, y_los - y)
            psi_d = chi_d + beta
            # teta is how pydyna_simple measures yaw (starting from west, spanning [0,2pi])
            self.des_yaw_msg.data = 1.57079632679 - psi_d # psi to theta (radians)
            self.des_velocity_msg.data = wv_next

            return (self.des_yaw_msg, self.des_velocity_msg)
        else:
            self.get_logger().info('Reached final waypoint Uhulll')
            self.des_yaw_msg.data = 0.0 # finishes pointing west
            self.des_velocity_msg.data = 0.0

            return (self.des_yaw_msg, self.des_velocity_msg)

def main(args=None):
    try:
        rclpy.init(args=args)
        los_guidance_node = LosGuidance()
        rclpy.spin(los_guidance_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except Exception as e:
        print(e)
    finally:
        los_guidance_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()