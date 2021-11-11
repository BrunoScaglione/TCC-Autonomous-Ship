import sys
import traceback

import numpy as np
from scipy.optimize import fsolve

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State, SurgeControl
from path_following_interfaces.srv import InitValues

class SurgeController(Node):
    def __init__(self):
        super().__init__('surge_controller_node')

        # controller parameters
        self.X_added_mass = -3375
        self.m = 40415
        # TODO: tune these
        self.phi_tuning_factor = 60
        self.kf_tuning_factor = 17 
        self.kf = self.kf_tuning_factor*13

        self.server_init_control = self.create_service(
            InitValues, '/init_surge_control', self.callback_init_control
        )

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_estimated_state = self.create_subscription(
            State,
            '/estimated_state',
            self.callback_estimated_state,
            1)

        self.subscription_desired_surge_velocity = self.create_subscription(
            SurgeControl,
            '/desired_surge_velocity',
            self.callback_desired_surge_velocity,
            1)

        self.publisher_propeller_thrust = self.create_publisher(
            Float32,
            '/propeller_thrust',
            1)

        self.thrust_msg = Float32()
    
    # tunes controller based on controller tuned for worst case scenario:
        # has to go from v=1 to v=3 from waypoint (0,0) to (500,500)
    def tune_controller(self, waypoints, initial_state):
        waypoints.position.x.insert(0, initial_state.position.x)
        waypoints.position.y.insert(0, initial_state.position.y)
        waypoints.velocity.insert(0, initial_state.velocity.u)
        cases = []
        for i in range(1, len(waypoints.velocity)):
            distance = (
                (waypoints.position.x[i] - waypoints.position.x[i-1])**2 +
                (waypoints.position.y[i] - waypoints.position.y[i-1])**2
            )**0.5
            delta_surge_velocity = (waypoints.velocity[i] - waypoints.velocity[i-1])
            cases.append(delta_surge_velocity/distance)
        worst_case = max(cases)
        # 0.00282842712 = (3 - 1)/sqrt(500^2 + 500^2)
        self.kf_tuning_factor = self.kf_tuning_factor*(worst_case/0.00282842712)
        
    def callback_init_control(self, req, res):
        self.tune_controller(req.waypoints, req.initial_state)
        self.desired_surge_velocity = req.surge
        self.desired_surge_velocity_old = req.initial_state.velocity.u
        self.delta_waypoints = (
            (req.waypoints.position.x[0] - req.initial_state.position.x)**2 +
            (req.waypoints.position.y[0] - req.initial_state.position.y)**2
        )**0.5
        thrust_msg = self.surge_control(req.initial_state.velocity.u)
        res.surge = thrust_msg.data
        return res

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
         
    def callback_estimated_state(self, msg):
        self.get_logger().info('listened estimated surge velocity: %f' % msg.velocity.u)
        thrust_msg = self.surge_control(msg.velocity.u)
        self.publisher_propeller_thrust.publish(thrust_msg)
        self.get_logger().info('published thrust force: %f' % thrust_msg.data)
    
    def callback_desired_surge_velocity(self, msg):
        self.get_logger().info('listened desired surge velocity: %f' % msg.desired_velocity)
        if self.desired_surge_velocity != msg.desired_velocity:
            self.desired_surge_velocity_old = self.desired_surge_velocity
            self.desired_surge_velocity = msg.desired_velocity
        self.delta_waypoints = msg.delta_waypoints
    
    def surge_control(self, xf): # x is surge velocity
        xf_d = self.desired_surge_velocity
        self.get_logger().info('xf_d: %f' % xf_d)
        xf_dold = self.desired_surge_velocity_old
        self.get_logger().info('xf_dold: %f' % xf_dold)
        # sliping variable
        s = xf - xf_d
        self.get_logger().info('s: %f' % s)
        # distace between waypoints
        distance = self.delta_waypoints
        self.get_logger().info('delta_waypoints: %f' % self.delta_waypoints)
        k = (self.kf*5.18*(10**-5) + 0.01)
        # estimated time to get from the old waypoint to the next
        # soltion of following equation
        # distance(t) = integral of velocity(t) from 0 to est_time (xf_dold*est_time + (xf_d - xf_dold)*(est_time + (1/k)*exp(-est_time*k)))
        # velocity(t) = xf_dold + (xf_d - xf_dold)*(1 - exp(-t*k))
        # distance(t) = (xf_dold*est_time + (xf_d - xf_dold)*(est_time + (1/k)*exp(-est_time*k)) -(1/k)*(xf_d - xf_dold))
        # distance = distance(t)
        est_time = self.get_est_time(distance, k, xf_dold, xf_d)[0]
        self.get_logger().info('est_time: %f' % est_time)
        # based on phi = 0.32 and k = 13*5.18*(10**-5) + 0.01 of controller i made for surge control project (from 0 to 5m/s)
        phi_as_percentage_of_k = 29.9810744468*k
        phi = self.phi_tuning_factor*phi_as_percentage_of_k*(self.kf*5.18*(10**-5) + (abs(xf_dold-xf_d)/est_time))
        self.get_logger().info('phi: %f' % phi)
        # sat function
        sats = max(-1,min(s/phi,1))
        self.get_logger().info('sats: %f' % sats)
        # input as function of x (control action)
        u = xf*abs(xf)*(1.9091*(10**-4) - self.kf*5.18*(10**-5)*sats) - (abs(xf_dold-xf_d)/est_time)*sats
        self.get_logger().info('u: %f' % u) 
        # thrust
        tau = u*(self.m - self.X_added_mass)
        self.thrust_msg.data = tau 
        return self.thrust_msg
    
    def get_est_time(self, distance, k, initial_velocity, final_velocity):
        data = (distance, k, initial_velocity, final_velocity)
        est_time = fsolve(self.func, (2*final_velocity + initial_velocity)/3, args=data)
        return est_time

    @staticmethod
    def func(t, *data):
        distance, k, initial_velocity, final_velocity = data
        return ( # expression == 0
            -distance + (initial_velocity*t + (final_velocity - initial_velocity)*(t + (1/k)*np.exp(-t*k)) - (1/k)*(final_velocity - initial_velocity))
        )
    
def main(args=None):
    try:
        rclpy.init(args=args)
        surge_controller_node = SurgeController()
        rclpy.spin(surge_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        surge_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()