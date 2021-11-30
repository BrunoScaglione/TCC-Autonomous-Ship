import sys
import traceback
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

        # could receive initial propeller rotation from init_simul msg
        # but not urgent now, can be done later
        self.propeller_rotation = 0

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

        self.subscription_propeller = self.create_subscription(
            Float32,
            '/propeller_rotation',
            self.callback_propeller_rotation,
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

    def callback_shutdown(self, _):
        sys.exit()
        

    def venus_init(self):
        # GET MAPQUEST API KEY
        self.viewer = venus.viewer.Venus(mapquest_key = "1bZQGGHqFLQBezmB29WKAHTJKBXM0wDl", logging=True, port=6150)
        # self.initial_position = GeoPos(-23.06255, -44.2772) # angra dos reis
        self.initial_position = GeoPos(-23.992557, -46.318) # santos 
        self.viewer.set_viewport(self.initial_position, 15)
        vessel_config = Vessel(
            position = self.initial_position,
            angle = 0,
            size = Size(32, 186.4),
            # could receive initial rudder angle from init_simul msg
            # but not urgent now, can be done later
            rudders=[Rudder(angle=0, length=0.1, visual_options={"color": "orange"})],
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
            data_panel= [
                KeyValue("ID", "104"),
                KeyValue("Width", "32 m"),
                KeyValue("Height", "186 m"),
                KeyValue("Linear Position X", "Waiting simul init"),
                KeyValue("Linear Position Y", "Waiting simul init"),
                KeyValue("Angular Position Theta", "Waiting simul init"),
                KeyValue("Linear Velocity U", "Waiting simul init"),
                KeyValue("Linear Velocity V", "Waiting simul init"),
                KeyValue("Angular Velocity R", "Waiting simul init"),
                KeyValue("Time", "Waiting simul init"),
                KeyValue("Rudder angle", "Waiting simul init"),
                KeyValue("Propeller rotation", "Waiting simul init")
            ]
        )
        self.vessel = self.viewer.add(vessel_config)
        self.viewer.on_object_drag_end = self.on_object_drag_end

    def callback_state(self, msg):
        state = msg
        self.get_logger().info(
            'listened state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                state.position.x, 
                state.position.y, 
                state.position.theta, # yaw angle
                state.velocity.u, 
                state.velocity.v, 
                state.velocity.r,
                state.time 
            )
        )
        #sleep(0.05)
        self.vessel.position = self.initial_position.relative(state.position.x, state.position.y)
        # measured from north clockwise (normal convention)
        self.vessel.angle = 90 - math.degrees(state.position.theta) # theta to psi

        # slice indexing was throwing error
        self.vessel.data_panel[3] = KeyValue("Linear Position X", str(round(state.position.x, 2)) + " m")
        self.vessel.data_panel[4] = KeyValue("Linear Position Y", str(round(state.position.y, 2)) + " m")
        self.vessel.data_panel[5] = KeyValue("Angular Position Theta", str(round(state.position.theta, 2)) + " rad (from east counterclockwise )")
        self.vessel.data_panel[6] = KeyValue("Linear Velocity U", str(round(state.velocity.u, 2)) + " m/s")
        self.vessel.data_panel[7] = KeyValue("Linear Velocity V", str(round(state.velocity.v, 2)) + " m/s")
        self.vessel.data_panel[8] = KeyValue("Angular Velocity R", str(round(state.velocity.r, 4)) + " rad/s (counterclockwise)")
        self.vessel.data_panel[9] = KeyValue("Time", str(round(state.time, 2)) + " s")
        self.vessel.data_panel[10] = KeyValue("Rudder angle", str(round(self.vessel.rudders[0].angle, 2)) + " deg (from south clockwise)")
        self.vessel.data_panel[11] = KeyValue("Propeller rotation", str(round(self.propeller_rotation, 2)) + " Hz")
    
    def callback_rudder_angle(self, msg):
        self.get_logger().info('listened rudder angle: %f' % msg.data)
        # measured from south clockwise (normal convention )
        self.vessel.rudders[0].angle = math.degrees(msg.data)

    def callback_propeller_rotation(self, msg):
        self.get_logger().info('listened propeller rotation: %f' % msg.data)
        self.propeller_rotation = msg.data

    def callback_waypoints(self, msg):
        # initial x,y,u
        msg.position.x.insert(0, 0)
        msg.position.y.insert(0, 0)
        msg.velocity.insert(0, 0) # FILLER (just to maintain same lenght of the lists)
        self.waypoints = msg # {position: {x: [...], y: [...]} velocity: [...]}
        
        num_waypoints = len(msg.position.x)
        self.get_logger().info('initial waypoint + listened %d waypoints' % (num_waypoints-1))

        # Draw in the map

        # lists inside: [object, GeoPos]
        # GeoPos is only here because there was a problem using 
        # the object's position to crate/update lines (need to investigate)
        self.beacons = [] 
        self.lines = []
        for i in range(num_waypoints):
            wx, wy, wv = msg.position.x[i], msg.position.y[i], msg.velocity[i]
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, wx, wy, wv))
            
            if i == 0:
                background_color = "green"
                beacon_data_panel = [KeyValue("Initial Position", "🏁")]
                draggable = False
            else:
                background_color = "red"
                beacon_data_panel = [
                    KeyValue("Waypoint", "📍"), 
                    KeyValue("Position X", str(wx)), 
                    KeyValue("Position Y",  str(wy)), 
                    KeyValue("Velocity U", str(wv)) 
                ]
                draggable = True

            beacon = Beacon(
                position=self.initial_position.relative(wx, wy),
                visual_options={
                    "background-color": background_color,
                    "border-radius": "50%"
                },
                data_panel=beacon_data_panel,
                draggable=draggable
            )
            self.viewer.add(beacon)
            # read below commented section tounderstand why i am doing this
            self.beacons.append([beacon, self.initial_position.relative(wx, wy)])

        ######### <passing beacon position inside points does not work, dont know why> ######
        # for j in range(num_waypoints):
        #     if j != num_waypoints-1:
        #         print(self.beacons[j][0].position.latitude)
        #       
        #         line = Line(
        #             points=[self.beacons[j][0].position, self.beacons[j+1][0].position],
        #             visual_options={"color": "yellow", "weight": 5}
        #         )
        #         self.viewer.add(line)
        #         self.lines.append(line)
        ######### <passing beacon position inside points does not work, dont know why/> ######

            if i != num_waypoints-1:
                wx_next, wy_next = msg.position.x[i+1], msg.position.y[i+1]
                line = Line(
                    points=[self.initial_position.relative(wx, wy), self.initial_position.relative(wx_next, wy_next)],
                    visual_options={"color": "yellow", "weight": 5}
                )
                self.viewer.add(line)
                self.lines.append(line)

    def on_object_drag_end(self, obj, new_position):
        num_beacons = len(self.beacons)
        beacons_objects = [el[0] for el in self.beacons]
        beacon_idx = beacons_objects.index(obj)
        if 0 < beacon_idx < num_beacons-1:
            line_before = self.lines[beacon_idx-1]
            line_after = self.lines[beacon_idx]

            new_line_before = Line(
                points=[self.beacons[beacon_idx-1][1], new_position],
                visual_options={"color": "yellow", "weight": 5},
                draggable=False
            )

            new_line_after = Line(
                points=[new_position, self.beacons[beacon_idx+1][1]],
                visual_options={"color": "yellow", "weight": 5},
                draggable=False
            )

            self.viewer.remove(line_before)
            self.viewer.remove(line_after)

            self.viewer.add(new_line_before)
            self.viewer.add(new_line_after)

            self.lines[beacon_idx-1] = new_line_before
            self.lines[beacon_idx] = new_line_after
        elif beacon_idx == 0:
            line_after = self.lines[beacon_idx]

            new_line_after = Line(
                points=[new_position, self.beacons[beacon_idx+1][1]],
                visual_options={"color": "yellow", "weight": 5},
                draggable=False
            )

            self.viewer.remove(line_after)
            self.viewer.add(new_line_after)
            self.lines[beacon_idx] = new_line_after
        else:
            line_before = self.lines[beacon_idx-1]

            new_line_before = Line(
                points=[self.beacons[beacon_idx-1][1], new_position],
                visual_options={"color": "yellow", "weight": 5},
                draggable=False
            )

            self.viewer.remove(line_before)
            self.viewer.add(new_line_before)
            self.lines[beacon_idx-1] = new_line_before

        self.beacons[beacon_idx][0].position = new_position
        self.beacons[beacon_idx][1] = new_position # just to pass inside lines
        # FILLERS: str(1) -> need to get relative coordinates back
        self.beacons[beacon_idx][0].data_panel[1] = KeyValue("Position X", str(1))
        self.beacons[beacon_idx][0].data_panel[2] = KeyValue("Position Y", str(1))
        
def main(args=None):
    try:
        rclpy.init(args=args)
        venus_node = Venus() # port 6150
        rclpy.spin(venus_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        venus_node.viewer.stop()
        venus_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()