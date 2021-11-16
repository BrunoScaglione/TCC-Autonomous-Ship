import os
import glob
import json
from datetime import datetime
import traceback

from flask import Flask, request

import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interfaces
from path_following_interfaces.msg import Waypoints 
from path_following_interfaces.srv import InitValues

class Backend(Node):
    def __init__(self):
        super().__init__('backend_node')

        self.declare_parameter('db_dir', './')
        self.db_dir = self.get_parameter('db_dir').get_parameter_value().string_value

        self.end_msg = Bool()
        self.end_msg.data = True
        self.shutdown_msg = Bool()
        self.shutdown_msg.data = True
        
        self.init_values_srv = InitValues.Request()
        self.waypoints_msg = Waypoints()

        waypoints = {'position': {}}
        waypoints['position']['x'] = list(self.waypoints_msg.position.x)
        waypoints['position']['y'] = list(self.waypoints_msg.position.y)
        waypoints['velocity'] = list(self.waypoints_msg.velocity)

        self.save_waypoints(waypoints)

        self.client_init_setpoints = \
            self.create_client(InitValues, '/init_setpoints')

        self.client_init_surge_control = \
            self.create_client(InitValues, '/init_surge_control')
        
        self.client_init_yaw_control = \
            self.create_client(InitValues, '/init_yaw_control')

        self.client_init_simul = \
            self.create_client(InitValues, '/init_simul')

        self.publisher_waypoints = self.create_publisher(
            Waypoints,
            '/waypoints',
            1)

        self.publisher_end = self.create_publisher(
            Bool,
            '/end',
            1)

        self.publisher_shutdown = self.create_publisher(
            Bool,
            '/shutdown',
            1)
    
    def save_waypoints(self, waypoints):
        now = datetime.now()
        time_stamp = now.strftime("%Y_%m_%d-%H_%M_%S")

        waypoints_dir = os.path.join(self.db_dir, 'waypoints')
        waypoints_path = os.path.join(waypoints_dir, f'waypoints_{time_stamp}.json')

        # clean before
        files = glob.glob(os.path.join(waypoints_dir, '*.json'))
        for f in files:
            os.remove(f) 

        with open(waypoints_path, 'w', encoding='utf-8') as f:
            json.dump(waypoints, f, ensure_ascii=False, indent=4)
    
    def log_state(self, state):
        self.get_logger().info(
            'Received from client initial state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}}' 
            % (
                state['position']['x'], 
                state['position']['y'], 
                state['position']['theta'], # yaw angle from west spanning [0, 2pi]
                state['velocity']['u'], 
                state['velocity']['v'], 
                state['velocity']['r'],
            )
        )

def wait_future(node, future_str):
    my_future = getattr(node, future_str)
    rclpy.spin_until_future_complete(node, my_future, timeout_sec=15)
    if my_future.done():
        try:
            return my_future.result(), 0
        except:
            return None, 0
    else:
        return None, 1

rclpy.init(args=None)
backend_node = Backend()

app = Flask(__name__)

@app.route("/waypoints", methods=['POST'])
def receive_waypoints():
    try:
        waypoints = request.json
        if not waypoints['from_gui']:
            backend_node.save_waypoints(waypoints)

            num_waypoints = len(waypoints['position']['x'])
            backend_node.get_logger().info('received from client %d waypoints' % num_waypoints)
            for i in range(num_waypoints):
                backend_node.get_logger().info(
                    'Received waypoint %d: %f %f %f' % 
                    (i, waypoints['position']['x'][i], waypoints['position']['y'][i], waypoints['velocity'][i])
                )

            backend_node.waypoints_msg.position.x = waypoints['position']['x']
            backend_node.waypoints_msg.position.y = waypoints['position']['y']
            backend_node.waypoints_msg.velocity = waypoints['velocity']

            backend_node.init_values_srv.waypoints.position.x = waypoints['position']['x']
            backend_node.init_values_srv.waypoints.position.y = waypoints['position']['y']
            backend_node.init_values_srv.waypoints.velocity = waypoints['velocity']

            backend_node.get_logger().info('Returning HTTP OK to client')
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
        else:
            # TODO: service for getting the updated waypoints from venus server
            pass
    except:
        backend_node.get_logger().info(
            "Waypoints received from client are not valid\n"
            "Returning HTTP bad request to client"
        )
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

@app.route("/initialCondition", methods=['POST'])
def receive_initial_condition():
    try:
        initial_condition = request.json

        backend_node.log_state(initial_condition)

        backend_node.init_values_srv.initial_state.position.x = \
            initial_condition['position']['x']
        backend_node.init_values_srv.initial_state.position.y = \
            initial_condition['position']['y']
        backend_node.init_values_srv.initial_state.position.theta = \
            initial_condition['position']['theta']
        backend_node.init_values_srv.initial_state.velocity.u = \
            initial_condition['velocity']['u']
        backend_node.init_values_srv.initial_state.velocity.v = \
            initial_condition['velocity']['v']
        backend_node.init_values_srv.initial_state.velocity.r = \
            initial_condition['velocity']['r']

        backend_node.get_logger().info('Returning HTTP OK to client')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info(
            "Initial condition received from client is not valid\n"
            "Returning HTTP bad request to client"
        )
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

@app.route("/start")
def start_system():
    try:
        backend_node.get_logger().info("Starting system")

        backend_node.publisher_waypoints.publish(backend_node.waypoints_msg)

        # get initial setpoints
        backend_node.future_init_setpoints = backend_node.client_init_setpoints. \
            call_async(backend_node.init_values_srv)
        res_setpoints, timeout_setpoints = wait_future(backend_node, "future_init_setpoints")
        delattr(backend_node, "future_init_setpoints")
        service_failed = False if timeout_setpoints else True

        # set initial setpoints and get initial control actions
        backend_node.init_values_srv.surge = res_setpoints.surge
        backend_node.future_init_surge_control = backend_node.client_init_surge_control. \
            call_async(backend_node.init_values_srv)
        res_surge_control, timeout_surge_control = wait_future(backend_node, "future_init_surge_control")
        delattr(backend_node, "future_init_surge_control")
        service_failed = False if not service_failed and not timeout_surge_control else True


        backend_node.init_values_srv.yaw = res_setpoints.yaw
        backend_node.future_init_yaw_control = backend_node.client_init_yaw_control. \
            call_async(backend_node.init_values_srv)
        res_yaw_control, timeout_yaw_control = wait_future(backend_node, "future_init_yaw_control")
        delattr(backend_node, "future_init_yaw_control")
        service_failed = False if not service_failed and not timeout_yaw_control else True

        # set inital state and control action of the simulation
        backend_node.init_values_srv.surge = res_surge_control.surge
        backend_node.init_values_srv.yaw = res_yaw_control.yaw
        backend_node.future_init_simul = backend_node.client_init_simul. \
            call_async(backend_node.init_values_srv)
        _, timeout_simul = wait_future(backend_node, "future_init_simul")
        delattr(backend_node, "future_init_simul")
        service_failed = False if not service_failed and not timeout_simul else True

        backend_node.get_logger().info('returning HTTP OK to client')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        if not service_failed:
            backend_node.get_logger().info('returning HTTP Gateaway timedout to client')
            return json.dumps({'success':False}), 504, {'ContentType':'application/json'}
        else:
            backend_node.get_logger().info('returning HTTP internal server error to client')
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

@app.route("/end")
def end_simul():
    try:
        backend_node.get_logger().info("Ending system")
        backend_node.publisher_end.publish(backend_node.end_msg)

        backend_node.get_logger().info('returning HTTP OK to client')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info('returning HTTP internal server error to client')
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

@app.route("/shutdown")
def shutdown_nodes(): 
    try:
        backend_node.get_logger().info("Shutting down nodes")
        backend_node.publisher_shutdown.publish(backend_node.shutdown_msg)

        backend_node.get_logger().info('Returning HTTP OK to client')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info('returning HTTP internal server error to client')
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

def main():
    try:
        app.run() # port 5000 by default
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except:
        print(traceback.format_exc())
    finally:
        backend_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()



