import sys
import os
import glob
import traceback

import numpy as np

import matplotlib.pyplot as plt

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import Control, State
from path_following_interfaces.srv import InitValues

class YawController(Node):
    def __init__(self):
        super().__init__('yaw_controller_node')

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value

        self.RUDDER_SAT = 0.610865 # 35 degrees

        self.TIME_STEP = 0.1

        self.rudder_angle_history = []

        self.last_rudder_angle = 0

        self.Kp = 1.6 # best: 1.6
        self.Kd = 65 # best: 65
        self.Ki = 0.00075  # best: 0.00075 # what i used when tuning surge controller:  0.000075 (antiwindup way), 0.00583 (old way)
        self.t_current_desired_yaw_angle = 0.1
        self.t_last_desired_yaw_angle = 0
        # for the integral action (acumulates error)
        self.theta_bar_int = 0
        self.integration_range = 0.1

        self.server_init_control = self.create_service(
            InitValues, '/init_yaw_control', self.callback_init_control
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

        self.subscription_desired_yaw_angle = self.create_subscription(
            Control,
            '/desired_yaw_angle',
            self.callback_desired_yaw_angle,
            1)

        self.publisher_rudder_angle = self.create_publisher(
            Float32,
            '/rudder_angle',
            1)

        self.rudder_msg = Float32()

    def callback_shutdown(self, _):
        sys.exit()

    def callback_init_control(self, req, res):
        self.waypoints = req.waypoints

        # format waypoints
        self.waypoints.position.x.insert(0, req.initial_state.position.x)
        self.waypoints.position.y.insert(0, req.initial_state.position.y)
        self.waypoints.velocity.insert(0, req.initial_state.velocity.u)

        self.desired_yaw_angle = req.yaw
        self.desired_yaw_angle_old = req.initial_state.position.theta
        rudder_msg = self.yaw_control(req.initial_state.position.theta, req.initial_state.velocity.r)
        res.yaw = rudder_msg.data
        self.last_rudder_angle = rudder_msg.data
        return res
        
    def callback_filtered_state(self, msg):
        self.get_logger().info('listened filtered yaw angle: %f' % msg.position.theta)
        self.publisher_rudder_angle.publish(self.rudder_msg)
        self.rudder_angle_history.append(self.rudder_msg.data)
        self.t = msg.time
        self.get_logger().info('time: %f' % msg.time)
        self.yaw_control(msg.position.theta, msg.velocity.r)
        self.get_logger().info('published rudder angle: %f' % self.rudder_msg.data)
    
    def callback_desired_yaw_angle(self, msg):
        self.get_logger().info('listened desired yaw angle: %f' % msg.desired_value)

        self.t_last_desired_yaw_angle = self.t_current_desired_yaw_angle
        self.t_current_desired_yaw_angle = self.t

        # fixes async issues
        # sometimes receives 2 desired yaw angles in sequence, without receiving filtered yaw angle
        if self.t_last_desired_yaw_angle == self.t_current_desired_yaw_angle:
           self.t_current_desired_yaw_angle += self.TIME_STEP
        
        if self.desired_yaw_angle != msg.desired_value:
            self.desired_yaw_angle_old = self.desired_yaw_angle
            self.desired_yaw_angle = msg.desired_value

    def pid(self, theta_bar, theta_bar_dot, integrator=True):
        if integrator:
            self.theta_bar_int = self.theta_bar_int + theta_bar*self.TIME_STEP
            self.get_logger().info('self.theta_bar_int: %f' % self.theta_bar_int)
            rudder_angle = -self.Kp*theta_bar - self.Kd*theta_bar_dot - self.Ki*self.theta_bar_int
        else:
            rudder_angle = -self.Kp*theta_bar - self.Kd*theta_bar_dot
        
        return rudder_angle

    def yaw_control(self, theta, r):
        # desired theta
        theta_des = self.desired_yaw_angle
        # last desired theta
        theta_des_old = self.desired_yaw_angle_old
        # error
        dif1 = theta - theta_des
        dif2 = theta - (6.28318530718 + theta_des)
        if abs(dif1) < abs(dif2):
            self.get_logger().info('used dif1: %f' % dif1)
            theta_bar = dif1
        else:
            self.get_logger().info('used dif2: %f' % dif2)
            theta_bar = dif2
        theta_bar = min(theta - theta_des, theta - (6.28318530718 - theta_des))
        self.get_logger().info('theta_bar: %f' % theta_bar)
        theta_bar_dot = r - (theta_des - theta_des_old)/ \
            (self.t_current_desired_yaw_angle - self.t_last_desired_yaw_angle)
        self.get_logger().info('theta_bar_dot: %f' % theta_bar_dot)

        # antiwindup stategy 1
        if abs(theta_bar) > self.integration_range:
            self.get_logger().info('### not using integrator because of integration range')
            rudder_angle =  self.pid(theta_bar, theta_bar_dot, integrator=False)
        else:
            self.get_logger().info('### normal pid using integrator')
            rudder_angle = self.pid(theta_bar, theta_bar_dot)

        # rudder saturation (with 1% safety margin)
        # real sat is 35 degress
        rudder_angle = max(-self.RUDDER_SAT*0.99, min(rudder_angle, self.RUDDER_SAT*0.99))
        self.rudder_msg.data = rudder_angle
        self.last_rudder_angle = rudder_angle
        
        return self.rudder_msg
    
    def generate_plots(self):
        #clean before
        files = glob.glob(os.path.join(self.plots_dir, 'rudderAngle*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = self.TIME_STEP*np.array(range(len(self.rudder_angle_history)))
        fig, ax = plt.subplots(1)
        ax.set_title("Rudder angle")
        ax.plot(t, self.rudder_angle_history)
        ax.set_xlabel("t [s]")
        ax.set_ylabel(r"$\delta\;[rad\;(from south clockwise)]$")
        ax.set_ylim(min(self.rudder_angle_history), max(self.rudder_angle_history))

        fig.savefig(os.path.join(self.plots_dir, "rudderAngle.png"))

def main(args=None):
    try:
        rclpy.init(args=args)
        yaw_controller_node = YawController()
        rclpy.spin(yaw_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        yaw_controller_node.get_logger().info('Stopped with user interrupt')
    except SystemExit:
        pass
    except:
        print(traceback.format_exc())
    finally:
        yaw_controller_node.generate_plots()
        yaw_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

# GRAVEYARD:
# -  for antiwindup strategy 2 (may be used in ther scenario)
    # [useful snippet in other situation] for antiwindup strategy 2 only:
    #     # cumulative of the error (integral action)
    #     theta_bar_int = self.theta_bar_int + theta_bar*self.TIME_STEP
    #     # self.theta_bar_int = max(-self.ANTIWINDUP, min(self.theta_bar_int,self.ANTIWINDUP))
    #     self.get_logger().info('self.theta_bar_int: %f' % theta_bar_int)
    #     # control action 
    #     rudder_angle = -self.Kp*self.K_tuning_factor*theta_bar - self.Kd*theta_bar_dot - self.Ki *theta_bar_int
        
    #     return rudder_angle, theta_bar*self.TIME_STEP

    # [useful snippet in other situation] antiwindup stategy 2 -> wasnt very succesfull in this case, but is generally good
    # if ( # saturated
    #     self.last_rudder_angle > self.RUDDER_SAT*0.99 or self.last_rudder_angle < -self.RUDDER_SAT*0.99
    # ): 
    #     # verify if the current control would increase the abs(self.theta_bar_int)
    #     self.get_logger().info('### doing antiwindup experiment with integrator')
    #     if self.last_rudder_angle*self.pid_using_integrator(theta_bar, theta_bar_dot, experiment=True)[1] > 0:
    #         # dont consider integral action
    #         self.get_logger().info('### not using antiwindup because would "saturate more"')
    #         rudder_angle = self.pid_not_using_integrator(theta_bar, theta_bar_dot)
    #     else:
    #         self.get_logger().info('### normal pid using integrator')
    #         rudder_angle = self.pid_using_integrator(theta_bar, theta_bar_dot)[0]
    # else:
    #     self.get_logger().info('### normal pid using integrator')
    #     rudder_angle = self.pid_using_integrator(theta_bar, theta_bar_dot)[0]

# - autotune controller
    # def tune_controller(self, waypoints, initial_state):
    #     cases = []
    #     self.desired_steady_state_yaw_angles = []
    #     for i in range(1, len(waypoints.velocity)):
    #         print(waypoints.position.x[i])
    #         print(waypoints.position.y[i])
    #         print(waypoints.position.x[i-1])
    #         print(waypoints.position.y[i-1])
    #         distance = (
    #             (waypoints.position.x[i] - waypoints.position.x[i-1])**2 +
    #             (waypoints.position.y[i] - waypoints.position.y[i-1])**2
    #         )**0.5
    #         desired_steady_state_yaw_angle = math.atan2(
    #             waypoints.position.y[i]-waypoints.position.y[i-1],
    #             waypoints.position.x[i]-waypoints.position.x[i-1]
    #         )

    #         self.desired_steady_state_yaw_angles.append(desired_steady_state_yaw_angle)
    #         if i != 1:
    #             self.get_logger().info(' i != 1:')
    #             last_desired_steady_state_yaw_angle = math.atan2(
    #                 waypoints.position.y[i-1]-waypoints.position.y[i-2],
    #                 waypoints.position.x[i-1]-waypoints.position.x[i-2]
    #             )
    #         else:
    #             self.get_logger().info('i == 1:')
    #             last_desired_steady_state_yaw_angle = initial_state.position.theta
    #         delta_yaw_angle = (
    #             abs(desired_steady_state_yaw_angle - last_desired_steady_state_yaw_angle)
    #         )
    #         try:
    #             case = delta_yaw_angle/distance
    #         except ZeroDivisionError:
    #             case = delta_yaw_angle
    #         cases.append(case)
    #     worst_case = max(cases)
    #     # 0.0011107205 = math.radians(90 - 45)/sqrt(500^2 + 500^2)
    #     auto_tuning_factor = worst_case/0.0011107205
    #     self.get_logger().info('yaw controller autotuning factor: %f' % auto_tuning_factor)
    #     self.K_tuning_factor = self.K_tuning_factor*auto_tuning_factor