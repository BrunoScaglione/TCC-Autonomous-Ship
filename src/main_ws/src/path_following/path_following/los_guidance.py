import sys
import os
import glob
import traceback

import matplotlib.pyplot as plt
import math
import numpy as np
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

        self.TIME_STEP = 0.1

        # los parameters
        self.SHIP_LENGHT = 186.4
        # los radius
        self.R = self.SHIP_LENGHT*2

        ###########################################
        # VERY IMPORTANT, CHANGING THIS VALUE ALLOWS TRADEOFF
        ## BETWEEN SMOOTH TRAJECTORY (higher value) AND REACHING WAYPOINTS PRECISELY
        # When craft is inside acceptance radius for a waypoint that
        # it considers waypoint was reached
        # tuned for:
        # self.R_ACCEPTANCE = 50 # use this for linear waypoints
        self.R_ACCEPTANCE = self.SHIP_LENGHT*2  # use this for zigzag waypoints
        ############################################

        # final radius of accceptance
        self.R_ACCEPTANCE_FINAL = 50

        # Size of radius around last waypoint. 
        # When craft is outside this radius it should have stopped
        # self.R_STOP = 100.0

        self.desired_values_history = {
            'values': [[],[]],
            'time': []
        }

        self.path_error = []
        self.width_error = []

        # When true, completed all waypoints
        self.no_more_waypoints = False

        # When true, craft is within self.R_ACCEPTANCE_FINAL of the final waypoint
        self.finished = False

        # index of waypoint the ship has to reach next (first waypoint is starting position)
        self.current_waypoint = 1
        
        self.des_yaw_msg = Control()
        # self.des_velocity_msg = Float32()
        self.des_velocity_msg = Control()

        self.shutdown_msg = Bool()
        self.shutdown_msg.data = True

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
        
        self.publisher_shutdown = self.create_publisher(
            Bool,
            '/shutdown',
            1)

    def callback_shutdown(self, _):
        sys.exit()

    def callback_init_setpoints(self, req, res):
        req.waypoints.position.x.insert(0, req.initial_state.position.x)
        req.waypoints.position.y.insert(0, req.initial_state.position.y)
        req.waypoints.velocity.insert(0, req.initial_state.velocity.u)
        self.waypoints = req.waypoints # {position: {x: [...], y: [...]} velocity: [...]}
        
        self.get_steady_state_yaw_angles(self.waypoints)

        self.num_waypoints = len(req.waypoints.position.x)
        self.get_logger().info('initial waypoint + listened %d waypoints' % (self.num_waypoints-1))
        for i in range(self.num_waypoints):
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, req.waypoints.position.x[i], req.waypoints.position.y[i], req.waypoints.velocity[i]))
        
        des_velocity_msg, des_yaw_msg = self.los(req.initial_state)
        res.surge, res.yaw = des_velocity_msg.desired_value, des_yaw_msg.desired_value
        return res

    def get_steady_state_yaw_angles(self, waypoints):
        self.desired_steady_state_yaw_angles = []
        for i in range(1, len(waypoints.velocity)):
            desired_steady_state_yaw_angle = math.atan2(
                waypoints.position.y[i]-waypoints.position.y[i-1],
                waypoints.position.x[i]-waypoints.position.x[i-1]
            )
            self.desired_steady_state_yaw_angles.append(desired_steady_state_yaw_angle)
        
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
        
    def reached_next_waypoint(self, xf, R_acceptance):
        x, y = xf.position.x, xf.position.y
        idx = self.current_waypoint
        wx_next , wy_next  = self.waypoints.position.x[idx], self.waypoints.position.y[idx]
        return 1 if (x-wx_next)**2 + (y-wy_next)**2 <= R_acceptance**2 else 0
    
    def missed_waypoint(self, xf):
        # when craft passes line that is orthogonal to los line and 
        # intercept the next waypoint
        # instead of going back trying to reach waypoint missed, 
        # craft will change to next waypoint
        x, y = xf.position.x, xf.position.y
        idx = self.current_waypoint
        wx, wy = self.waypoints.position.x[idx-1], self.waypoints.position.y[idx-1]
        wx_next , wy_next = self.waypoints.position.x[idx], self.waypoints.position.y[idx]

        if (wx_next - wx) == 0:
            self.get_logger().info('1')
            passed_wnext = True if (wy_next-wy)*(y - wy_next) > 0 else False
        elif (wy_next - wy) == 0:
            passed_wnext = True if (wx_next-wx)*(x - wx_next) > 0 else False
        else:
            c = (wy_next - wy)/(wx_next - wx)
            self.get_logger().info('c: %f' % c)
            a_wnext = -1/c
            b_wnext = wy_next - a_wnext*wx_next

            passed_wnext = True if (wx_next-wx)*a_wnext*(a_wnext*x + b_wnext - y) > 0 \
                else False

        self.get_logger().info('passed_wnext: True') if passed_wnext else \
            self.get_logger().info('passed_wnext: False')
            
        return passed_wnext 

    def get_xy_los(self, x, y, wx, wy, wx_next, wy_next):
        
        x_los, y_los = symbols('x_los, y_los')
        eq1 = Eq((x_los-x)**2 + (y_los-y)**2, self.R**2)

        if (wx_next - wx) == 0:
            eq2 = Eq(x_los, wx)
        elif (wy_next - wy) == 0:
            eq2 = Eq(y_los, wy)
        else:
            eq2 = Eq(((wy_next - wy)/(wx_next - wx)), (y_los - wy)/(x_los - wx))

        sol = solve([eq1, eq2], [x_los, y_los])
        soln = [tuple(v.evalf() for v in s) for s in sol] # evaluated numerically

        x_los1, y_los1 = soln[0]
        self.get_logger().info('x_los1: %f, y_los1: %f' % (x_los1, y_los1))
        x_los2, y_los2 = soln[1]
        self.get_logger().info('x_los2: %f, y_los2: %f' % (x_los2, y_los2))

        # dot product -> projection of (los intercept - craft positio) vector
        # onto los line vector (connecting waypoints)
        (x_los, y_los) = (x_los1, y_los1) if (wx_next-wx)*(x_los1-x) + (wy_next-wy)*(y_los1-y) > 0 else (x_los2, y_los2)
        
        self.get_logger().info('wx_next: %f' % wx_next)
        self.get_logger().info('x_los: %f, y_los: %f' % (x_los, y_los))

        return (x_los, y_los)

    def get_current_width_error(self, idx, theta):
        if math.radians(90) < theta < math.radians(180) or math.radians(270) < theta < math.radians(360):
            self.get_logger().info('theta = %f : in second or forth quadrants' % theta)
            zeta = math.radians(90) - self.desired_steady_state_yaw_angles[idx-1]
            beta = math.radians(90) - zeta
            alfa = beta - (theta - math.radians(90))
            self.get_logger().info('alfa: %f' % alfa)
            if self.path_error[-1] == 0:
                if math.radians(90) < theta < math.radians(180):
                    return self.path_error[-1] + abs((self.SHIP_LENGHT/2)*np.cos(alfa))
                else:
                    return self.path_error[-1] - abs((self.SHIP_LENGHT/2)*np.cos(alfa))
            elif self.path_error[-1] > 0:
                return self.path_error[-1] + abs((self.SHIP_LENGHT/2)*np.cos(alfa))
            else:
                return self.path_error[-1] + -abs((self.SHIP_LENGHT/2)*np.cos(alfa))
        else:
            self.get_logger().info('theta = %f : in first or third quadrants' % theta)
            chi = theta - self.desired_steady_state_yaw_angles[idx-1]
            alfa = math.radians(90) - chi
            self.get_logger().info('alfa: %f' % alfa)
            if self.path_error[-1] == 0:
                if 0 <= theta <= math.radians(90):
                    return self.path_error[-1] + abs((self.SHIP_LENGHT/2)*np.cos(alfa))
                else:
                    return self.path_error[-1] - abs((self.SHIP_LENGHT/2)*np.cos(alfa))
            elif self.path_error[-1] > 0:
                return self.path_error[-1] + abs((self.SHIP_LENGHT/2)*np.cos(alfa))
            else:
                return self.path_error[-1] + -abs((self.SHIP_LENGHT/2)*np.cos(alfa))
    
    def append_current_errors(self, x, y, theta, wx, wy, wx_next, wy_next):
        idx = self.current_waypoint
        use_current_waypoint = True
        if idx > 1: 
            # cx + d is line connecting waypoints
            # ax +  b is orthogonal to cx + d, passing through a waypoint or through the craft
            wx_before, wy_before = self.waypoints.position.x[idx-2], self.waypoints.position.y[idx-2]

            calc_intercept_result_with_check = self.calc_intercept(x, y, wx_before, wy_before, wx, wy, check=True)
            if calc_intercept_result_with_check[3]:
                (xi, yi, positive_error, _) = self.calc_intercept(x, y, wx, wy, wx_next, wy_next)
            else:
                use_current_waypoint = False
                (xi, yi, positive_error, _) = calc_intercept_result_with_check
        else:
            (xi, yi, positive_error, _) = self.calc_intercept(x, y, wx, wy, wx_next, wy_next)

        current_path_error = ((x - xi)**2 + (y - yi)**2)**0.5
        if not positive_error:
            current_path_error = - current_path_error
        self.get_logger().info('current_path_error: %f' % current_path_error)

        self.path_error.append(current_path_error)

        if use_current_waypoint:
            current_width_error = self.get_current_width_error(idx, theta)
        else:
            current_width_error = self.get_current_width_error(idx-1, theta)

        self.width_error.append(current_width_error)

    @staticmethod
    def calc_intercept(x, y, wx1, wy1, wx2, wy2, check=False):
        if check:
            xi = None
            yi = None
            positive_error = None
            not_between_waypoints = False
            if (wy1 - wy2) == 0:
                if (wx2-wx1)*(x-wx2) < 0:
                    xi = x
                    yi = wy2

                    positive_error = True if y > wy1 else False
                else:
                    not_between_waypoints = True
            elif (wx1 - wx2) == 0:
                if (wy2-wy1)*(y-wy2) < 0:
                    xi = wx2
                    yi = y

                    positive_error = True if x < wx1 else False
                else:
                    not_between_waypoints = True
            else:
                c = (wy1 - wy2)/(wx1 - wx2)
                d = wy1 - c*wx1   
                a = -1/c              
                b = y - a*x
                e = wy2 - a*wx2
                
                if (wx2 - wx1)*a*(a*x + e - y) < 0:
                    # craft changed from waypoint a to waypoint b, but hasnt passed 
                    # waypoint a yet, so error will be relative to line that goes to waypoint a
                    # waypoint a is w, waypoint b is w_next, and waypoint before a is w_before
                    xi = (b - d)/(c - a)
                    yi = c*xi + d

                    positive_error = True if y > yi else False
                else:
                    not_between_waypoints = True

            return (xi, yi, positive_error, not_between_waypoints)

        else:
            if (wy1 - wy2) == 0:
                xi = x
                yi = wy2

                positive_error = True if y > wy1 else False
    
            elif (wx1 - wx2) == 0:
                xi = wx2
                yi = y

                positive_error = True if x < wx1 else False
            else:
                c = (wy1 - wy2)/(wx1 - wx2)
                d = wy1 - c*wx1   
                a = -1/c              
                b = y - a*x
                # craft changed from waypoint a to waypoint b, but hasnt passed 
                # waypoint a yet, so error will be relative to line that goes to waypoint a
                # waypoint a is w, waypoint b is w_next, and waypoint before a is w_before
                xi = (b - d)/(c - a)
                yi = c*xi + d

                positive_error = True if y > yi else False

            return (xi, yi, positive_error, None)

    def los(self, xf):
        if not self.no_more_waypoints:
            if self.reached_next_waypoint(xf, self.R_ACCEPTANCE) or self.missed_waypoint(xf):
                if self.current_waypoint == self.num_waypoints - 1:
                    self.no_more_waypoints = True
                else:
                    self.current_waypoint += 1
                    self.get_logger().info('changed waypoint at time: %f' % xf.time)
        else:
            self.finished = True if self.reached_next_waypoint(xf, self.R_ACCEPTANCE_FINAL) else False

        idx = self.current_waypoint
        x, y, theta = xf.position.x, xf.position.y, xf.position.theta
        u, v = xf.velocity.u, xf.velocity.v
        U = (u**2 + v**2)**0.5
        wx_next, wy_next, wv_next = self.waypoints.position.x[idx], self.waypoints.position.y[idx], self.waypoints.velocity[idx]
        wx, wy = self.waypoints.position.x[idx-1], self.waypoints.position.y[idx-1]
            
        if not self.finished:
            # Find x_los and y_los by solving 2 eq.
            # Analytic solution:
            # 1. isolating x_los
            # ((wy - wy_past)/(wx - wx_past))*(x_los - wx) == (y_los - wy)
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))
            # 2.  substitute and solve for y_los
            # (x_los-wx)**2 + (y_los-wy)**2 == self.R**2
            # 3.  get x_los
            # x_los == ((y_los - wy) + wx*((wy - wy_past)/(wx - wx_past)))/((wy - wy_past)/(wx - wx_past))

            x_los, y_los = self.get_xy_los(x, y, wx, wy, wx_next, wy_next)
            beta = math.asin(v/U)
            chi_d = math.atan2(x_los - x, y_los - y)
            psi_d = chi_d + beta

            # theta is how pydyna_simple measures yaw (starting from west, spanning [0,2pi])
            desired_value = 1.57079632679 - psi_d # psi to theta (radians)
            # format to positive angles
            if desired_value < 0:
                desired_value = 6.28318530718 + desired_value

            self.des_yaw_msg.desired_value = desired_value
            self.des_velocity_msg.desired_value = wv_next

            distance_waypoints = ((wx_next - wx)**2 + (wy_next - wy)**2)**0.5
            self.get_logger().info('wx_next: %f' % wx_next)
            self.get_logger().info('wx: %f' % wx)
            self.get_logger().info('distance_waypoints: %f' % distance_waypoints)
            self.des_yaw_msg.distance_waypoints = distance_waypoints
            self.des_velocity_msg.distance_waypoints = distance_waypoints
        else:
            # Will shutdown all nodes when reached final waypoint
            self.publisher_shutdown.publish(self.shutdown_msg)

        # norm of vector from craft location to path, making 90 degrees with path line
        self.append_current_errors(x, y, theta, wx, wy, wx_next, wy_next)

        self.desired_values_history['values'][0].append(self.des_velocity_msg.desired_value)
        self.desired_values_history['values'][1].append(self.des_yaw_msg.desired_value)
        
        self.desired_values_history['time'].append(xf.time)

        self.des_velocity_msg.current_waypoint, self.des_yaw_msg.current_waypoint = idx, idx

        return (self.des_velocity_msg, self.des_yaw_msg)
    
    def generate_plots(self):
        #clean before
        files = glob.glob(os.path.join(self.plots_dir, 'setpoints', '*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = self.desired_values_history['time']
        
        ss_dir = "setpoints"
        desired_values_props = [
            {
                "title": "Linear Veloicity U Setpoint",
                "ylabel": r"$u_{des}\;[m/s]$",
                "file": "linearvelocityUSetpoint.png"
            },
            {
                "title": "Angular Position Theta Setpoint",
                "ylabel": r"$\theta_{des}\;[rad]$",
                "file": "angularpositionThetaSetpoint.png"
            },
        ]

        for i in range(len(self.desired_values_history['values'])):
            fig, ax = plt.subplots(1)
            ax.set_title(desired_values_props[i]["title"])
            ax.plot(t, self.desired_values_history['values'][i])
            ax.set_xlabel(r"$t\;[s]$")
            ax.set_ylabel(desired_values_props[i]["ylabel"])
            # ax.set_ylim(min(self.desired_values_history['values'][i]), max(self.desired_values_history['values'][i]))

            fig.savefig(os.path.join(self.plots_dir, ss_dir, desired_values_props[i]["file"]))


        # Program may be interrupted when self.path_error was already updated (appended value)
        # but t was not
        if len(self.path_error) > len(t):
            self.path_error = self.path_error[:-1]

        if len(self.width_error) > len(t):
            self.width_error = self.width_error[:-1]

        # clean before
        files = glob.glob(os.path.join(self.plots_dir, 'errors', 'error*.png'))
        for f in files:
            os.remove(f)
        
        fig, ax = plt.subplots(1)
        ax.set_title("Path error")
        ax.plot(t, self.path_error)
        ax.set_xlabel("t [s]")
        ax.set_ylabel("path error [m]")
        # ax.set_ylim(min(self.path_error), max(self.path_error))
        fig.savefig(os.path.join(self.plots_dir, "errors", "errorPath.png"))

        fig, ax = plt.subplots(1)
        ax.set_title("Width error")
        ax.plot(t, self.width_error)
        ax.set_xlabel("t [s]")
        ax.set_ylabel("width error [m]")
        # ax.set_ylim(min(self.width_error), max(self.width_error))
        fig.savefig(os.path.join(self.plots_dir, "errors", "errorWidth.png"))

        ######## report plots

        # clean before
        files = glob.glob(os.path.join(self.plots_dir, "reportPlots", "losGuidance", '*.png'))
        for f in files:
            os.remove(f)

        fig, ax = plt.subplots(1)
        ax.set_title("Errors")
        ax.plot(t, self.path_error)
        ax.plot(t, self.width_error)
        ax.set_xlabel("t [s]")
        ax.set_ylabel("error [m]")
        ax.legend([r"$cross-track$ error", r"$width$ error"])
        fig.savefig(os.path.join(self.plots_dir, "reportPlots", "losGuidance", "errors.png"))

    def print_metrics(self):
        mean_path_error = np.mean(np.abs(self.path_error))
        print('Mean path error: ', mean_path_error)
        self.get_logger().info('Mean path error: %f' % mean_path_error)

        max_path_error = np.max(np.abs(self.path_error))
        print('Max path error: ', max_path_error)
        self.get_logger().info('Max path error: %f' % max_path_error)

        mean_width_error = np.mean(np.abs(self.width_error))
        print('Mean width error: ', mean_width_error)
        self.get_logger().info('Mean width error: %f' % mean_width_error)
        
        max_width_error = np.max(np.abs(self.width_error))
        print('Max width error: ', max_width_error)
        self.get_logger().info('Max width error: %f' % max_width_error)

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
        
def main(args=None):
    try:
        rclpy.init(args=args)
        los_guidance_node = LosGuidance()
        rclpy.spin(los_guidance_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        los_guidance_node.get_logger().info('Stopped with user interrupt')
    except SystemExit:
        if los_guidance_node.finished:
            print('Finished path')
            los_guidance_node.get_logger().info('Finished path')
        else:
            print('Stopped with user shutdown request')
            los_guidance_node.get_logger().info('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        los_guidance_node.print_metrics()
        los_guidance_node.generate_plots()
        los_guidance_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()