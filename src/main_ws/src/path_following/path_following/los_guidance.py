import sys
import os
import traceback

import matplotlib.pyplot as plt
import math
from sympy import symbols, Eq, solve
# import stackprinter

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
#custom service
from path_following_interfaces.msg import State, Control
from path_following_interfaces.srv import InitValues

class LosGuidance(Node):
    def __init__(self):
        super().__init__('los_guidance_node')

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value

        self.desired_values_history = [[],[]]

        self.TIME_STEP = 0.1

        # los parameters
        self.SHIP_LENGHT = 186
        # los radius
        self.R = self.SHIP_LENGHT*2 
        # When craft is inside acceptance radius for a waypoint that
        # it considers waypoint was reached
        self.R_ACCEPTANCE = 50 
        # Size of radius around last waypoint. 
        # When craft is outside this radius it should have stopped
        self.R_STOP = 100.0

        # When true, completed all waypoints
        self.finished = False

        # index of waypoint the ship has to reach next (first waypoint is starting position)
        self.current_waypoint = 1
        
        self.des_yaw_msg = Control()
        # self.des_velocity_msg = Float32()
        self.des_velocity_msg = Control()

        self.server_init_setpoints = self.create_service(
            InitValues, '/init_setpoints', self.callback_init_setpoints
        )

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

        self.publisher_desired_yaw_angle = self.create_publisher(
            Control,
            '/desired_yaw_angle',
            1)

        self.publisher_desired_surge_velocity = self.create_publisher(
            Control,
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

    def callback_init_setpoints(self, req, res):
        req.waypoints.position.x.insert(0, req.initial_state.position.x)
        req.waypoints.position.y.insert(0, req.initial_state.position.y)
        req.waypoints.velocity.insert(0, req.initial_state.velocity.u)
        self.waypoints = req.waypoints # {position: {x: [...], y: [...]} velocity: [...]}
        
        self.num_waypoints = len(req.waypoints.position.x)
        self.get_logger().info('initial waypoint + listened %d waypoints' % (self.num_waypoints-1))
        for i in range(self.num_waypoints):
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, req.waypoints.position.x[i], req.waypoints.position.y[i], req.waypoints.velocity[i]))
        
        des_velocity_msg, des_yaw_msg = self.los(req.initial_state)
        res.surge, res.yaw = des_velocity_msg.desired_value, des_yaw_msg.desired_value
        return res

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
        
    def callback_filtered_state(self, msg):
        try: # need have received waypoints first
            self.log_state(msg)
            des_velocity_msg, des_yaw_msg = self.los(msg)
            self.publisher_desired_yaw_angle.publish(des_yaw_msg)
            self.get_logger().info('published desired yaw angle: %f' % des_yaw_msg.desired_value)
            self.publisher_desired_surge_velocity.publish(des_velocity_msg)
            self.get_logger().info('published desired velocity: %f' % des_velocity_msg.desired_value)
        except AttributeError:
            self.get_logger().info('Has not received waypoints yet, will ignore listened state')
        
    def reached_next_waypoint(self, xf):
        x, y = xf.position.x, xf.position.y
        idx = self.current_waypoint
        wx_next , wy_next  = self.waypoints.position.x[idx], self.waypoints.position.y[idx]
        return 1 if (x-wx_next)**2 + (y-wy_next)**2 < self.R_ACCEPTANCE**2 else 0

    def get_xy_los(self, x, y, wx_next, wy_next, wx, wy):
        x_los, y_los = symbols('x_los, y_los')
        eq1 = Eq((x_los-x)**2 + (y_los-y)**2, self.R**2)
        eq2 = Eq(((wy_next - wy)/(wx_next - wx)), (y_los - wy)/(x_los - wx))

        sol = solve([eq1, eq2], [x_los, y_los])
        soln = [tuple(v.evalf() for v in s) for s in sol] # evaluated numerically

        x_los1, y_los1 = soln[0]
        self.get_logger().info('x_los1: %f, y_los1: %f' % (x_los1, y_los1))
        x_los2, y_los2 = soln[1]
        self.get_logger().info('x_los2: %f, y_los2: %f' % (x_los2, y_los2))

        (x_los, y_los) = (x_los1, y_los1) if (wx_next-x)*(x_los1-x) > 0 else (x_los2, y_los2)
        
        #debugging
        self.get_logger().info('wx_next: %f' % wx_next)
        self.get_logger().info('x_los: %f, y_los: %f' % (x_los, y_los))

        return (x_los, y_los)
    
    def los(self, xf):
        if not self.finished:
            if self.reached_next_waypoint(xf):
                if self.current_waypoint == self.num_waypoints - 1:
                    self.finished = True
                else:
                    self.current_waypoint += 1
                    self.get_logger().info('changed waypoint at time: %f' % xf.time)
            
            if not self.finished:
                idx = self.current_waypoint
                x, y = xf.position.x, xf.position.y
                u, v = xf.velocity.u, xf.velocity.v
                U = (u**2 + v**2)**0.5
                wx_next, wy_next, wv_next = self.waypoints.position.x[idx], self.waypoints.position.y[idx], self.waypoints.velocity[idx]
                wx, wy = self.waypoints.position.x[idx-1], self.waypoints.position.y[idx-1]

                # Find x_los and y_los by solving 2 eq.
                # Analytic solution:
                # 1. isolating x_los
                # ((wy - wy_past)/(wx - wx_past))*(x_los - wx) == (y_los - wy)
                # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))
                # 2.  substitute and solve for y_los
                # (x_los-wx)**2 + (y_los-wy)**2 == self.R**2
                # 3.  get x_los
                # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))

                x_los, y_los = self.get_xy_los(x, y, wx_next, wy_next, wx, wy)
                beta = math.asin(v/U)
                chi_d = math.atan2(x_los - x, y_los - y)
                psi_d = chi_d + beta
                # teta is how pydyna_simple measures yaw (starting from west, spanning [0,2pi])
                self.des_yaw_msg.desired_value = 1.57079632679 - psi_d # psi to theta (radians)
                self.des_velocity_msg.desired_value = wv_next

                distance_waypoints = ((wx_next - wx)**2 + (wy_next - wy)**2)**0.5
                self.get_logger().info('wx_next: %f' % wx_next)
                self.get_logger().info('wx: %f' % wx)
                self.get_logger().info('distance_waypoints: %f' % distance_waypoints)
                self.des_yaw_msg.distance_waypoints = distance_waypoints
                self.des_velocity_msg.distance_waypoints = distance_waypoints
            else:
                self.get_logger().info('Reached final waypoint Uhulll')
                self.des_yaw_msg.desired_value = 0.0 # finishes pointing west
                self.des_velocity_msg.desired_value = 0.0

                self.des_yaw_msg.distance_waypoints = self.R_STOP
                self.des_velocity_msg.distance_waypoints = self.R_STOP
        else:
            self.get_logger().info('Reached final waypoint Uhulll')
            self.des_yaw_msg.desired_value = 0.0 # finishes pointing west
            self.des_velocity_msg.desired_value = 0.0

            self.des_yaw_msg.distance_waypoints = self.R_STOP
            self.des_velocity_msg.distance_waypoints = self.R_STOP

        

        self.desired_values_history[0].append(self.des_velocity_msg.desired_value)
        self.desired_values_history[1].append(self.des_yaw_msg.desired_value)

        return (self.des_velocity_msg, self.des_yaw_msg)
    
    def generate_plots(self):
        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = [self.TIME_STEP*i for i in range(len(self.desired_values_history[0]))]
        ss_dir = "setpoints"
        desired_values_props = [
            {
                "title": "Linear Veloicity U Setpoint",
                "ylabel": r"u_{des}\;[m/s]",
                "file": "linearvelocityUSetpoint.png"
            },
            {
                "title": "Angular Position Theta Setpoint",
                "ylabel": r"\theta_{des}\;[rad]",
                "file": "angularpositionThetaSetpoint.png"
            },
        ]

        for i in range(len(self.desired_values_history)):
            fig, ax = plt.subplots(1)
            ax.set_title(desired_values_props[i]["title"])
            ax.plot(t, self.desired_values_history[i])
            ax.set_xlabel(r"t\;[s]")
            ax.set_ylabel(desired_values_props[i]["ylabel"])
            ax.set_ylim([min(self.desired_values_history[i]), max(self.desired_values_history[i])])

            fig.savefig(os.path.join(self.plots_dir, ss_dir, desired_values_props[i]["file"]))

def main(args=None):
    try:
        rclpy.init(args=args)
        los_guidance_node = LosGuidance()
        rclpy.spin(los_guidance_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        los_guidance_node.generate_plots()
        los_guidance_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()