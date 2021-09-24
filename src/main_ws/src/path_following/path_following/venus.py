import math
from time import sleep

import pydyna
import venus.viewer
from venus.objects import (
    GeoPos, Rudder, Vessel, Size, KeyValue, Button
)

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
# custom interface
from path_following_interfaces.msg import State

class Venus(Node):
    def __init__(self):
        super().__init__('venus_node')

        self.venus_init()

        self.subscription_state = self.create_subscription(
            State,
            '/state',
            self.callback_state,
            1)

        # obs: this wasnt in the initial schematic
        self.subscription_state = self.create_subscription(
            Float32,
            '/rudder_angle',
            self.callback_rudder_angle,
            1)

    def venus_init(self):
        # GET MAPQUEST API KEY
        self.viewer = venus.viewer.Venus(mapquest_key = "1bZQGGHqFLQBezmB29WKAHTJKBXM0wDl", logging=True, port=6150)
        self.initial_position = GeoPos(-23.06255, -44.2772) # angra dos reis
        self.viewer.set_viewport(self.initial_position, 15)
        vessel_config = Vessel(
            position = self.initial_position,
            angle = 0,
            size = Size(32, 186),
            rudders=[Rudder(angle=0, length=0.1, visual_options={"color": "red"})],
            visual_options={
                "stroke": True,
                "color": "green",  # stroke color
                "weight": 3,  # stroke weight
                "opacity": 1.0,  # stroke opacity
                "lineCap": "round",
                "lineJoin": "round",
                "dashArray": None,
                "dashOffset": None,
                "fill": True,
                "fillColor": "red",
                "fillOpacity": 0.2,
                "fillRule": "evenodd",
            },
            data_panel=[
                KeyValue("ID", "0"),
                KeyValue("Width", "32"),
                KeyValue("Height", "186"),
                Button("btn_vessel", "Click here"),
            ],
        )
        self.vessel = self.viewer.add(vessel_config)

    def callback_state(self, msg):
        state = msg
        self.get_logger().info(
            'listened state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                state.position.x, 
                state.position.y, 
                state.position.psi, # yaw angle
                state.velocity.u, 
                state.velocity.v, 
                state.velocity.r,
                state.time 
            )
        )
        #sleep(0.05)
        self.vessel.position = self.initial_position.relative(state.position.x, state.position.y)
        self.vessel.angle = math.degrees(state.position.psi)
    
    def callback_rudder_angle(self, msg):
        self.get_logger().info('listened rudder angle: %f' % msg.data)
        self.vessel.rudders[0].angle = math.degrees(msg.data)

def main(args=None):
    try:
        rclpy.init(args=args)
        venus_node = Venus()
        rclpy.spin(venus_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    finally:
        venus_node.viewer.stop()
        venus_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()