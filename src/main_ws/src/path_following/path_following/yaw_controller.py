import sys

import math

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

        #parameters
        self.K_tuning_factor = 1
        self.Kp = self.K_tuning_factor*1.34
        self.Kd = 49.684
        self.Ki = 0.00583
        self.rudder_sat = 0.610865
        self.t_current_desired_yaw_angle = 0.1
        self.t_last_desired_yaw_angle = 0
        # for the integral action (acumulates error)
        self.theta_bar_int = 0

        self.server_init_control = self.create_service(
            InitValues, '/init_yaw_control', self.callback_init_control
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
    
    def tune_controller(self, waypoints, initial_state):
        waypoints.position.x.insert(0, initial_state.position.x)
        waypoints.position.y.insert(0, initial_state.position.y)
        waypoints.velocity.insert(0, initial_state.velocity.u)
        cases = []
        self.desired_steady_state_yaw_angles = []
        for i in range(1, len(waypoints.velocity)):
            distance = (
                (waypoints.position.x[i] - waypoints.position.x[i-1])**2 +
                (waypoints.position.y[i] - waypoints.position.y[i-1])**2
            )**0.5
            desired_steady_state_yaw_angle = math.atan2(
                waypoints.position.y[i]-waypoints.position.y[i-1],
                waypoints.position.x[i]-waypoints.position.x[i-1]
            )
            self.desired_steady_state_yaw_angles.append(desired_steady_state_yaw_angle)
            try:
                last_desired_steady_state_yaw_angle = math.atan2(
                    waypoints.position.y[i-1]-waypoints.position.y[i-2],
                    waypoints.position.x[i-1]-waypoints.position.x[i-2]
                )
            except IndexError:
                last_desired_steady_state_yaw_angle = initial_state.position.theta
            delta_yaw_angle = (
                desired_steady_state_yaw_angle - last_desired_steady_state_yaw_angle
            )
            cases.append(delta_yaw_angle/distance)
        worst_case = max(cases)
        # 0.0011107205 = math.radians(90 - 45)/sqrt(500^2 + 500^2)
        self.K_tuning_factor = self.K_tuning_factor*(worst_case/0.0011107205)

    def callback_init_control(self, req, res):
        self.tune_controller(req.waypoints, req.initial_state)
        self.desired_yaw_angle = req.yaw
        self.desired_yaw_angle_old = req.initial_state.position.theta
        rudder_msg = self.yaw_control(req.initial_state.position.theta, req.initial_state.velocity.r)
        res.yaw = rudder_msg.data
        return res

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
        
    def callback_estimated_state(self, msg):
        self.get_logger().info('listened estimated yaw angle: %f' % msg.position.theta)
        self.t = msg.time
        rudder_msg = self.yaw_control(msg.position.theta, msg.velocity.r)
        self.publisher_rudder_angle.publish(rudder_msg)
        self.get_logger().info('published rudder angle: %f' % rudder_msg.data)
    
    def callback_desired_yaw_angle(self, msg):
        self.get_logger().info('listened desired yaw angle: %f' % msg.desired_value)

        self.t_last_desired_yaw_angle = self.t_current_desired_yaw_angle
        self.t_current_desired_yaw_angle = self.t

        # fixes async issues
        # sometimes receives 2 desired yaw angles in sequence, without receiving estimated yaw angle
        if self.t_last_desired_yaw_angle == self.t_current_desired_yaw_angle:
           self.t_current_desired_yaw_angle += 0.1
        
        if self.desired_yaw_angle != msg.desired_value:
            self.desired_yaw_angle_old = self.desired_yaw_angle
            self.desired_yaw_angle = msg.desired_value

    def yaw_control(self, theta, r):
        # desired theta
        theta_des = self.desired_yaw_angle
        # last desired theta
        theta_des_old = self.desired_yaw_angle_old
        # error
        theta_bar = theta - theta_des
        self.get_logger().info('theta_bar: %f' % theta_bar)
        theta_bar_dot = r - (theta_des - theta_des_old)/ \
            (self.t_current_desired_yaw_angle - self.t_last_desired_yaw_angle)
        # cumulative of the error (integral action)
        self.theta_bar_int = self.theta_bar_int + theta_bar*0.1
        # anti windup for the integral action
        self.theta_bar_int = max(-0.5,min(self.theta_bar_int,0.5))
        self.get_logger().info('self.theta_bar_int: %f' % self.theta_bar_int)

        # control action 
        rudder_angle = -self.Kp * theta_bar - self.Kd * theta_bar_dot - self.Ki * self.theta_bar_int
        # rudder saturation
        rudder_angle = max(-self.rudder_sat, min(rudder_angle, self.rudder_sat))
        self.rudder_msg.data = rudder_angle

        return self.rudder_msg 

def main(args=None):
    try:
        rclpy.init(args=args)
        yaw_controller_node = YawController()
        rclpy.spin(yaw_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except Exception as e:
        print(e)
    finally:
        yaw_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()