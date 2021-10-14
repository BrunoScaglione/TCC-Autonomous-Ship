import sys
import math

import venus.viewer
from venus.objects import (
    GeoPos, 
    Rudder, 
    Vessel,
    Beacon,
    Size, 
    KeyValue,
    Line
)

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import Waypoints, State

class Venus(Node):
    def __init__(self):
        super().__init__('venus_node')

        self.venus_init()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_state = self.create_subscription(
            State,
            '/state',
            self.callback_state,
            1)

        self.subscription_rudder = self.create_subscription(
            Float32,
            '/rudder_angle',
            self.callback_rudder_angle,
            1)

        self.subscription_waypoints = self.create_subscription(
            Waypoints,
            '/waypoints',
            self.callback_waypoints,
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
    
    def callback_shutdown():
        sys.exit()
    
    def callback_rudder_angle(self, msg):
        self.get_logger().info('listened rudder angle: %f' % msg.data)
        self.vessel.rudders[0].angle = math.degrees(msg.data)

    def callback_waypoints(self, msg):
        # initial x,y,u
        msg.position.x.insert(0, 0)
        msg.position.y.insert(0, 0)
        msg.velocity.insert(0, 0) # FILLER (just to maintain same lenght of the lists)
        self.waypoints = msg # {position: {x: [...], y: [...]} velocity: [...]}
        num_waypoints = len(msg.position.x)
        self.get_logger().info('listened %d waypoints' % num_waypoints)

        # draw in the map
        self.beacons = []
        self.lines = []
        for i in range(num_waypoints):
            wx, wy, wv = msg.position.x[i], msg.position.y[i], msg.velocity[i]
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, wx, wy, wv))
            
            if i == 0:
                background_color = "green"
                beacon_data_panel = [KeyValue("Initial Position", "🏁")]
            else:
                background_color = "red"
                beacon_data_panel = [
                    KeyValue("Waypoint", "📍"), 
                    KeyValue("Position X", str(wx)), 
                    KeyValue("Position Y",  str(wy)), 
                    KeyValue("Velocity U", str(wv)) 
                ]

            beacon = self.viewer.add(
                Beacon(
                    position=self.initial_position.relative(wx, wy),
                    visual_options={
                        "background-color": background_color,
                        "border-radius": "50%"
                    },
                    data_panel=beacon_data_panel,
                    draggable=True
                )
            )
            self.beacons.append(beacon)

            # couldnt use beacon.position
            if i != num_waypoints-1:
                wx_next, wy_next = msg.position.x[i+1], msg.position.y[i+1]
                line = self.viewer.add(
                    Line(
                        points=[self.initial_position.relative(wx, wy), self.initial_position.relative(wx_next, wy_next)],
                        visual_options={"color": "yellow", "weight": 5},
                        draggable=False
                    )
                )
            self.lines.append(line)
            
def main(args=None):
    try:
        rclpy.init(args=args)
        venus_node = Venus() # port 6150
        rclpy.spin(venus_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except Exception as e:
        print(e)
    finally:
        venus_node.viewer.stop()
        venus_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()