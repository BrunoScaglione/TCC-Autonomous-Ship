import sys
import os
import glob
import traceback
import math

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State, Control
from path_following_interfaces.srv import InitValues

class SurgeController(Node):
    def __init__(self):
        super().__init__('surge_controller_node')

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value 

        self.TIME_STEP = 0.1

        self.X_ADDED_MASS = -3375
        self.M = 40415

        self.KF_CONSTANT = 13

        self.thrust_history = []

        self.phi_slope_tuning_factor = 10**-10 # without waves: 10**-10 
        self.phi_offset_tuning_factor = -0.13 # -0.13 without waves: -0.13 
        
        self.kf_constant_tuning_factor = 12 # 8 without waves: 3.4 

        self.est_time_correct_tuning_factor = 0.7

        self.server_init_control = self.create_service(
            InitValues, '/init_surge_control', self.callback_init_control
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

        self.subscription_desired_surge_velocity = self.create_subscription(
            Control,
            '/desired_surge_velocity',
            self.callback_desired_surge_velocity,
            1)

        self.publisher_propeller_thrust = self.create_publisher(
            Float32,
            '/propeller_thrust',
            1)

        self.thrust_msg = Float32()

    def callback_shutdown(self, _):
        sys.exit()
        
    def callback_init_control(self, req, res):
        self.waypoints = req.waypoints
        self.initial_state = req.initial_state

        # format waypoints
        self.waypoints.position.x.insert(0, self.initial_state.position.x)
        self.waypoints.position.y.insert(0, self.initial_state.position.y)
        self.waypoints.velocity.insert(0, self.initial_state.velocity.u)

        self.current_waypoint = 1

        self.last_waypoint_yaw_angle = self.initial_state.position.theta
        self.last_waypoint_surge_velocity = self.initial_state.velocity.u
        self.last_waypoint_sway_velocity = self.initial_state.velocity.v

        self.last_xu_d = self.waypoints.velocity[1]

        self.get_steady_state_yaw_angles(self.waypoints)

        self.desired_surge_velocity = req.surge
        self.desired_surge_velocity_old = self.initial_state.velocity.u
        self.distance_waypoints = (
            (self.waypoints.position.x[1] - self.initial_state.position.x)**2 +
            (self.waypoints.position.y[1] - self.initial_state.position.y)**2
        )**0.5
        self.get_logger().info('initial distance_waypoints: %f' % self.distance_waypoints)
        thrust_msg = self.surge_control(self.initial_state)
        res.surge = thrust_msg.data
        return res
         
    def callback_filtered_state(self, msg):
        self.get_logger().info('listened filtered surge velocity: %f' % msg.velocity.u)
        self.publisher_propeller_thrust.publish(self.thrust_msg)
        self.thrust_history.append(self.thrust_msg.data)
        self.surge_control(msg)
        self.get_logger().info('published thrust force: %f' % self.thrust_msg.data)
    
    def callback_desired_surge_velocity(self, msg):
        self.get_logger().info('listened desired surge velocity: %f' % msg.desired_value)
        if self.desired_surge_velocity != msg.desired_value:
            self.desired_surge_velocity_old = self.desired_surge_velocity
            self.desired_surge_velocity = msg.desired_value

        self.distance_waypoints = msg.distance_waypoints
        self.get_logger().info('updated distance_waypoints: %f' % self.distance_waypoints)

        self.current_waypoint = msg.current_waypoint
    
    def surge_control(self, xf): 
        # xu is surge velocity
        xu = xf.velocity.u
        xu_d = self.desired_surge_velocity
        self.get_logger().info('xu_d: %f' % xu_d)
        xu_dold = self.desired_surge_velocity_old
        self.get_logger().info('xu_dold: %f' % xu_dold)

        if xu_d != self.last_xu_d:
            self.last_waypoint_surge_velocity = xu
            self.last_waypoint_yaw_angle = xf.position.theta
            self.last_waypoint_sway_velocity = xf.velocity.v

            self.last_xu_d = xu_d

        # sliping variable
        s = xu - xu_d
        self.get_logger().info('s: %f' % s)
        # distace between waypoints
        distance = self.distance_waypoints
        self.get_logger().info('distance_waypoints: %f' % self.distance_waypoints)
        # estimated time to get from the old waypoint to the next
        # solution of following equation
        # distance(t) = integral of velocity(t) from 0 to est_time (xway_dold*est_time + (xu_d - xway_dold)*(est_time + (1/k)*exp(-est_time*k)))
        # velocity(t) = xway_dold + (xu_d - xway_dold)*(1 - exp(-t*k))
        # distance(t) = (xway_dold*est_time + (xu_d - xway_dold)*(est_time + (1/k)*exp(-est_time*k)) -(1/k)*(xu_d - xway_dold))
        kf = self.kf_constant_tuning_factor*(self.KF_CONSTANT)
        est_time = self.get_est_time(distance, kf, self.last_waypoint_surge_velocity, xu_d)
        self.get_logger().info('est_time: %f' % est_time)
        F = kf*5.18*(10**-5)
        eta = abs(self.last_waypoint_surge_velocity-xu_d)/est_time
        k = F + eta
        self.get_logger().info('k: %f' % k)
        # 0.0106734 is the baseline k (kf=13, from 0 to 5m/s in 500s) from my surge control project
        # 0.32 is the baseline phi from my surge control project
        phi = self.phi_slope_tuning_factor*k + (0.32 - self.phi_slope_tuning_factor*0.0106734) + self.phi_offset_tuning_factor
        self.get_logger().info('phi: %f' % phi)
        # sat function
        sats = max(-1, min(s/phi, 1))
        # sats = np.sign(s) # for tuning only 
        self.get_logger().info('sats: %f' % sats)
        # input as function of x (control action)
        f_hatp = xu*abs(xu)*1.9091*(10**-4)
        u = f_hatp - k*sats
        self.get_logger().info('u: %f' % u) 
        # thrust
        tau = u*(self.M - self.X_ADDED_MASS)
        self.thrust_msg.data = tau 

        return self.thrust_msg

    def get_steady_state_yaw_angles(self, waypoints):
        self.desired_steady_state_yaw_angles = []
        for i in range(1, len(waypoints.velocity)):
            desired_steady_state_yaw_angle = math.atan2(
                waypoints.position.y[i]-waypoints.position.y[i-1],
                waypoints.position.x[i]-waypoints.position.x[i-1]
            )
            self.desired_steady_state_yaw_angles.append(desired_steady_state_yaw_angle)
    
    def get_est_time(self, distance, kf, initial_velocity, final_velocity):
        data = (distance, kf, initial_velocity, final_velocity)
        est_time_exp = fsolve(self.func, (2*final_velocity + initial_velocity)/3, args=data)[0]
        est_time_lin = distance/((initial_velocity+final_velocity)/2)
        est_time = (est_time_lin + est_time_exp)/2
        # ponderates between linear and exponential response
        # when phi is higher goes from linear to exponential
        # but the claculation depends on knowing phi, which depend on k which depends on est_time itself
        # so, begins with a guess for est_time and runs 5 iterations
        for _ in range(5):
            k = (kf*5.18*(10**-5) + (abs(initial_velocity-final_velocity)/(est_time)))
            phi_bootstrap = self.phi_slope_tuning_factor*k + (0.32 - self.phi_slope_tuning_factor*0.0106734) + self.phi_offset_tuning_factor
            est_time = (((final_velocity-initial_velocity) - phi_bootstrap)*est_time_lin + phi_bootstrap*est_time_exp)/(final_velocity-initial_velocity)

        steady_state_yaw_angle = self.desired_steady_state_yaw_angles[self.current_waypoint-1]
        u_ss = final_velocity
        theta_change_basis = (self.last_waypoint_yaw_angle - steady_state_yaw_angle)
        v_ss = (
            np.cos(np.pi/2 - theta_change_basis)*self.last_waypoint_surge_velocity
            + np.cos(theta_change_basis)
        ) 

        # vss is used as velocity perpendicular to path(of the actual waypoint) at last waypoint 
        # uss is used as final surge velocity
        beta = math.asin(v_ss/(v_ss**2 + u_ss**2)**0.5)
        craft_steady_state_yaw_angle = steady_state_yaw_angle - beta

        # used the results obtained from when there wasnt estimated time correction as baseline for
        # self.est_time_correct_tuning_factor
        # at th begginging the estimated timme was 347 and the actual time was 275 to reach the waypoint
        # with initial surge velocity = 1 and initial yaw angle = 90 for linear waypoints 
        # 347 =  self.est_time_correct_tuning_factor*1.125*1*347
        est_time_corrected = self.est_time_correct_tuning_factor*((self.last_waypoint_yaw_angle - craft_steady_state_yaw_angle)/2*np.pi + 1)*self.last_waypoint_surge_velocity*est_time

        return est_time_corrected

    def generate_plots(self):
        #clean before
        files = glob.glob(os.path.join(self.plots_dir, 'thrustForce*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = self.TIME_STEP*np.array(range(len(self.thrust_history)))
        fig, ax = plt.subplots(1)
        ax.set_title("Thrust force")
        ax.plot(t, self.thrust_history)
        ax.set_xlabel("t [s]")
        ax.set_ylabel(r"$\tau_1\;[N]$")
        ax.set_ylim(min(self.thrust_history), max(self.thrust_history))

        graphics_file = "thrustForce.png"
        fig.savefig(os.path.join(self.plots_dir, graphics_file))

    @staticmethod
    def func(t, *data):
        distance, kf, initial_velocity, final_velocity = data
        return ( # expression == 0
            - distance + (initial_velocity*t + (final_velocity - initial_velocity)
            *(t + (1/(kf*5.18*(10**-5) + (abs(initial_velocity-final_velocity)/t)))
            *np.exp(-t*(kf*5.18*(10**-5) + (abs(initial_velocity-final_velocity)/t))))
            - (1/(kf*5.18*(10**-5) + (abs(initial_velocity-final_velocity)/t)))
            *(final_velocity - initial_velocity))
        )

    
def main(args=None):
    try:
        rclpy.init(args=args)
        surge_controller_node = SurgeController()
        rclpy.spin(surge_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        surge_controller_node.get_logger().info('Stopped with user interrupt')
    except SystemExit:
        pass
    except:
        print(traceback.format_exc())
    finally:
        surge_controller_node.generate_plots()
        surge_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()