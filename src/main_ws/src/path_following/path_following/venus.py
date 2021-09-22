from time import sleep

import pydyna
import venus.viewer

import rclpy
from rclpy.node import Node

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

    def venus_init():
        self.viewer = venus.viewer.Venus(mapquest_key = "API_KEY_HERE", logging=True, port=6150)
        self.initial_position = venus.objects.GeoPos(-23.06255, -44.2772) # angra dos reis
        self.viewer.set_viewport(initial_position, 15)
        vessel_config = venus.objects.Vessel(
            position = initial_position,
            angle = 0,
            size = venus.objects.Size(32, 186),
            rudders=[Rudder(angle=0, length=0.1, visual_options={"color": "red"})],
            visual_options={
                "stroke": True,
                "color": "#3388ff",  # stroke color
                "weight": 3,  # stroke weight
                "opacity": 1.0,  # stroke opacity
                "lineCap": "round",
                "lineJoin": "round",
                "dashArray": None,
                "dashOffset": None,
                "fill": True,
                "fillColor": "#3388ff",
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
        self.get_logger().info(
            'listened state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                msg.position.x, 
                msg.position.y, 
                msg.position.psi, # yaw angle
                msg.velocity.u, 
                msg.velocity.v, 
                msg.velocity.r,
                msg.time 
            )
        )
        sleep(0.05)
        self.vessel.position = self.initial_position.relative(msg.position.x, msg.position.y)
        self.vessel.angle = math.degrees(msg.velocity.r)

def main(args=None):
    rclpy.init(args=args)
    venus_node = Venus()
    
    rclpy.spin(venus_node)

    venus_node.viewer.stop()
    venus_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()