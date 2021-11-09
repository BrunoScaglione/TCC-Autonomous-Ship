import sys
# import traceback

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
        self.phi_tuning_factor = 40
        self.kf_tuning_factor = 17.5 
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

    def callback_init_control(self, req, res):
        self.desired_surge_velocity = req.surge
        self.desired_surge_velocity_old = req.initial_state.velocity.u
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
        # estimated time to get from the old waypoint to the next
        est_time = (abs(xf_dold-xf_d)/2)*distance
        # based on phi = 0.32 and kf = 13 of controller imade for surge control project (from 0 to 5m/s)
        phi_as_percentage_of_k = 0.32/(13*5.18*(10**-5) + 0.01)
        phi = self.phi_tuning_factor*phi_as_percentage_of_k*(self.kf*5.18*(10**-5) + (abs(xf_dold-xf_d)/est_time))
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
    
def main(args=None):
    try:
        rclpy.init(args=args)
        surge_controller_node = SurgeController()
        rclpy.spin(surge_controller_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    # except:
    #     print(traceback.format_exc())
    finally:
        surge_controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()