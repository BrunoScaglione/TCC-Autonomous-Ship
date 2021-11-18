import sys
import os
import numpy as np

import traceback

import pydyna

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State
#custom service
from path_following_interfaces.srv import InitValues

class PydynaSimpleNode(Node):

    def __init__(self):
        super().__init__('pydyna_simple_node')

        self.TIME_STEP = 0.1

        # need to declare them before
        self.declare_parameter('pkg_dir', './')
        self.declare_parameter('pkg_share_dir', './')
        # this will be overwritten by launch file
        self.declare_parameter('p3d_file', './') 

        self.pkg_dir = self.get_parameter('pkg_dir').get_parameter_value().string_value
        self.pkg_share_dir = self.get_parameter('pkg_share_dir').get_parameter_value().string_value
        self.p3d_file = self.get_parameter('p3d_file').get_parameter_value().string_value

        self.num_simul = 0
        self.end_simul = 0

        self.subscription_end = self.create_subscription(
            Bool,
            '/end',
            self.callback_end,
            1)

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.server_init_simul = self.create_service(InitValues, '/init_simul', self.callback_init_simul)

        self.subscription_propeller = self.create_subscription(
            Float32,
            '/propeller_rotation',
            self.callback_propeller,
            1)

        self.subscription_rudder = self.create_subscription(
            Float32,
            '/rudder_angle',
            self.callback_rudder,
            1)

        self.publisher_state = self.create_publisher(State, 'state', 1)
    
    def callback_end(self):
        self.get_logger().info('User requested simulation to end')
        sys.exit()
    
    def callback_shutdown(self, _):
        sys.exit()

    def callback_init_simul(self, req, res):
        if self.num_simul != 0:
            pydyna.destroy_report(self.rpt)

        self.get_logger().info('Initializing Simulation')
        
        # self.propeller_rotation = 0
        # self.rudder_angle = 0
        self.propeller_rotation = req.surge
        self.rudder_angle = req.yaw
        self.subscriptions_synced = False

        self.rpt = pydyna.create_text_report(os.path.join(self.pkg_share_dir, 'logs', 'pydynalogs', f'pydyna_log_{self.num_simul}'))
        self.sim = pydyna.create_simulation(os.path.join(self.pkg_dir, 'config', self.p3d_file))
        
        self.ship = self.sim.vessels['104']
        x, y, theta = req.initial_state.position.x, req.initial_state.position.y, req.initial_state.position.theta
        u, v, r = req.initial_state.velocity.u, req.initial_state.velocity.v, req.initial_state.velocity.r
        self.ship.linear_position = [x, y, 0]
        self.ship.angular_position = [0, 0, theta]
        self.ship.linear_velocity = [u, v, 0]
        self.ship.angular_velocity = [0, 0, r]
        self.proppeler_counter = 0
        self.rudder_counter = 0

        self.num_simul += 1

        self.state = req.initial_state
        self.log_state('server')

        return res
    
    def callback_propeller(self, msg):
        self.get_logger().info('listened propeller rotation: %f' % msg.data)
        self.propeller_rotation = msg.data
        self.proppeler_counter += 1
    
    def callback_rudder(self, msg):
        self.get_logger().info('listened rudder angle: %f' % msg.data)
        self.rudder_angle = msg.data
        self.rudder_counter += 1
    
    def extrapolate_state(self):
        propeller = self.ship.thrusters['0']
        propeller.dem_rotation = self.propeller_rotation
        rudder = self.ship.rudders['0']
        # pydyna uses counterclockwise convention
        rudder.dem_angle = -self.rudder_angle 

        self.sim.step()

        self.state.position.x = self.ship.linear_position[0]
        self.state.position.y = self.ship.linear_position[1]
        self.state.position.theta = self.ship.angular_position[2]%(2*np.pi)
        self.state.velocity.u = self.ship.linear_velocity[0]
        self.state.velocity.v = self.ship.linear_velocity[1]
        self.state.velocity.r = self.ship.angular_velocity[2]

        self.state.time += self.TIME_STEP

    def publish_state(self):
        self.publisher_state.publish(self.state)
        self.rpt.write(self.state.time, self.ship)
        self.log_state('publisher')

    def log_state(self, communicator):
        log_str = 'responded request with inital' if communicator == 'server' else 'published'
        self.get_logger().info(
            '%s state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                log_str,
                self.state.position.x, 
                self.state.position.y, 
                self.state.position.theta, # yaw angle
                self.state.velocity.u, 
                self.state.velocity.v, 
                self.state.velocity.r,
                self.state.time 
            )
        )
    
def main(args=None):
    try:
        rclpy.init(args=args)
        my_pydyna_node = PydynaSimpleNode()
        my_pydyna_node.get_logger().info('started main')
        while rclpy.ok():
            my_pydyna_node.get_logger().info('entered rclpy.ok loop')
            rclpy.spin_once(my_pydyna_node)
            if my_pydyna_node.proppeler_counter == my_pydyna_node.rudder_counter:
                if not my_pydyna_node.subscriptions_synced:
                    my_pydyna_node.extrapolate_state()
                    my_pydyna_node.publish_state()
                    my_pydyna_node.subscriptions_synced = True
            else:
                my_pydyna_node.subscriptions_synced = False
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except:
        print(traceback.format_exc())
    finally:       
        my_pydyna_node.get_logger().info('Ended Simulation')
        my_pydyna_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
