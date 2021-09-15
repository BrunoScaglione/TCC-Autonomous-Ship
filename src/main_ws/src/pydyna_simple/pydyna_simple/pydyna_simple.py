import pydyna

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
# custom interface
from path_following_interfaces.msg import State
#custom service
from path_following_interfaces.srv import StartSimul

class PydynaSimpleNode(Node):

    def __init__(self):
        super().__init__('pydyna_simple_node')
        self.new_simul = False

        self.server = self.create_service(StartSimul, 'start_simul', self.callback_start_simul)

        self.subscription_propeller = self.create_subscription(
            Float32,
            'propeller_rotation',
            self.callback_propeller,
            10)
        self.subscription_propeller  # prevent unused variable warning

        self.subscription_rudder = self.create_subscription(
            Float32,
            'rudder_angle',
            self.callback_rudder,
            1)
        self.subscription_rudder  # prevent unused variable warning

        self.publisher_state = self.create_publisher(State, 'state', 1)

    def callback_start_simul(self, req, res):
        self.new_simul = True
        self.sim = pydyna.create_simulation('./config/TankerL186B32_T085.p3d')
        self.ship = sim.vessels['104']
        # DONT KNOW IF THIS WILL RELY ALTER WHAT PYDYNA IS USING INTERNALLY
        self.ship.linear_position = [req.position.x, req.position.y, 0]
        self.ship.angular_position = [0, 0, req.position.psi]
        self.ship.linear_velocity = [req.velocity.u, req.velocity.v, 0]
        self.ship.angular_velocity = [0, 0, req.velocity.r]
        # typical initial state -> {position: {x:0, y:0, psi:0}, velocity: {u:0, v:0, r:0}}
        self.proppeler_counter = 0
        self.rudder_counter = 0

        self.state = req.initial_state
        self.log_state(self.state, 'server')

        res.aknowledged = 1
        return res
    
    def callback_propeller(self, msg):
        self.get_logger().info('listened propeller rotation: %f' % msg.data)
        # store proppeler rotation input
        self.propeller_rotation = msg.data
        self.proppeler_counter += 1
    
    def callback_rudder(self, msg):
        self.get_logger().info('listened rudder angle: %f' % msg.data)
        # store proppeler rotation input
        self.rudder_angle = msg.data
        self.rudder_counter += 1
    
    def extrapolate_state(self):
        propeller = ship.thrusters['0']
        propeller.dem_rotation = self.propeller_rotation
        rudder = ship.rudders['0']
        rudder.dem_angle = ship.rudders['0']

        sim.step()

        # FILLER [0,0,0],[1,1,1],[2,2,2],[3,3,3]
        #self.state = self.format_state([0,0,0],[1,1,1],[2,2,2],[3,3,3])
        self.state = self.format_state(
            ship.linear_position, 
            ship.angular_position,
            ship.linear_velocity,
            ship.angular_velocity 
        )

    def publish_state(self):
        self.publisher_state.publish(self.state)
        self.log_state(self.state, 'publisher')

    @staticmethod
    def format_state(ship_lin_pos, ship_ang_pos, ship_lin_vel, ship_ang_vel):
        threedof_pos = ship_lin_pos[0:2] + ship_ang_pos[3]
        threedof_vel = ship_lin_vel[0:2] + ship_ang_vel[3]
        position = {
            key: value for key, value in list(zip([u,v,r], threedof_pos))
        }
        velocity = {
            key: value for key, value in list(zip([x,y,psi], threedof_vel)) 
        }
        return {position, velocity}

    @staticmethod
    def log_state(state, communicator):
        log_str = 'responded request for inital' if communicator == 'server' else 'publisher'
        self.get_logger().info(
            '%s state: { \
            position: {x: %f, y: %f, psi: %f}, \
            velocity:{u: %f ,v: %f, r: %f} \
            }' % (
                log_str,
                state.position.x, 
                state.position.y, 
                state.position.psi, # yaw angle
                state.velocity.u, 
                state.velocity.v, 
                state.velocity.r 
                )
        )

def main(args=None):
    rclpy.init(args=args)
    my_pydyna_node = PydynaSimpleNode()
    subscriptions_not_synced = False

    while rclpy.ok():
        rclpy.spin_once(my_pydyna_node)
        prop_count = my_pydyna_node.proppeler_counter
        rudd_count = my_pydyna_node.rudder_counter
        if prop_count  != rudd_count:
            subscriptions_not_synced = True
        elif subscriptions_not_synced:
            subscriptions_not_synced = False
            my_pydyna_node.extrapolate_state()
            my_pydyna_node.publish_state()

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
