import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

# custom interface
from path_following_interfaces.msg import State

class PydynaSimpleNode(Node):

    def __init__(self):
        super().__init__('pydyna_simple_node')
        self.msg = State()

        self.state = {position: {x:0, y:0, psi:0}, velocity: {u:0, }}

        self.proppeler_counter = 0
        self.rudder_counter = 0


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
    
    def set_state(self):
        prop_rot = self.propeller_rotation
        rud_ang = self.rudder_angle

        # RUN ONE STEP OF PYDYNA SIMULATION HERE

        # self.state = self.format_state(
        #     ship.linear_position, 
        #     ship.angular_position,
        #     ship.linear_velocity,
        #     ship.angular_velocity 
        # )

        # FILLER [0,0,0],[1,1,1],[2,2,2],[3,3,3]
        self.state = self.format_state([0,0,0],[1,1,1],[2,2,2],[3,3,3])
    
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

    def publish_state(self):
        self.state_msg = self.state
        self.publisher_state.publish(self.state_msg)
        self.get_logger().info(
            'published state: { \
                position: {x: %f, y: %f, psi: %f}, \
                velocity:{u: %f ,v: %f, r: %f} \
            }' % (
                    msg.position.x, 
                    msg.position.y, 
                    msg.position.psi, 
                    msg.velocity.u, 
                    msg.velocity.v, 
                    msg.velocity.r 
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
            my_pydyna_node.set_state()
            my_pydyna_node.publish_state()

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
