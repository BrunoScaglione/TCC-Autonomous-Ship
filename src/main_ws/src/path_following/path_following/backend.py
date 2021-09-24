import json

from flask import Flask, request

import rclpy
from rclpy.node import Node

from path_following_interfaces.srv import Waypoints, StartEndSimul

class Backend(Node):
    def __init__(self):
        super().__init__('backend_node')
        self.client_start_end_simul = \
            self.create_client(StartEndSimul, '/start_end_simul')
        self.client_waypoints = self.create_client(Waypoints, '/waypoints')
        self.start_end_simul_srv = StartEndSimul.Request()
        self.waypoints_srv = Waypoints.Request()

        client_start_end_simul = self.create_client(StartEndSimul, '/start_end_simul')
        client_waypoints = self.create_client(Waypoints, '/waypoints')

def wait_future(node, node_future):
    rclpy.spin_once(node, timeout_sec=5)
    if node_future.done():
        try:
            return node_future.result(), 0
        except:
            return None, 0
    else:
        return None, 1

def log_initial_state(node, initial_state):
    node.get_logger().info(
        'Received from client initial state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}}' 
        % (
            initial_state['position']['x'], 
            initial_state['position']['y'], 
            initial_state['position']['psi'], # yaw angle
            initial_state['velocity']['u'], 
            initial_state['velocity']['v'], 
            initial_state['velocity']['r'],
        )
    )

rclpy.init(args=None)
backend_node = Backend()

app = Flask(__name__)

@app.route("/waypoints", methods=['POST'])
def receive_waypoints():
    try:
        waypoints = request.json

        num_waypoints = len(waypoints['position']['x'])
        backend_node.get_logger().info('received from client %d waypoints' % num_waypoints)
        for i in range(num_waypoints):
            backend_node.get_logger().info(
                'Received waypoint %d: %f %f %f' % 
                (i, waypoints['position']['x'][i], waypoints['position']['y'][i], waypoints['velocity'][i])
            )

        backend_node.waypoints_srv.position.x = waypoints['position']['x']
        backend_node.waypoints_srv.position.y = waypoints['position']['y']
        backend_node.waypoints_srv.velocity = waypoints['velocity']

        backend_node.get_logger().info('Returning HTTP OK to client')
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info(
            "Waypoints received from client are not valid\n"
            "Returning HTTP bad request to client"
        )
        return json.dumps({'success':False}), 400, {'ContentType':'application/json'}

@app.route("/initial_condition", methods=['POST'])
def receive_inital_condition():
    try:
        initial_condition = request.json

        log_initial_state(backend_node, initial_condition)

        backend_node.start_end_simul_srv.initial_state.position.x = \
            initial_condition['position']['x']
        backend_node.start_end_simul_srv.initial_state.position.y = \
            initial_condition['position']['y']
        backend_node.start_end_simul_srv.initial_state.position.psi = \
            initial_condition['position']['psi']
        backend_node.start_end_simul_srv.initial_state.velocity.u = \
            initial_condition['velocity']['u']
        backend_node.start_end_simul_srv.initial_state.velocity.v = \
            initial_condition['velocity']['v']
        backend_node.start_end_simul_srv.initial_state.velocity.r = \
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
        backend_node.start_end_simul_srv.end_simul = False

        backend_node.get_logger().info("Starting system")

        future_start_simul = backend_node.client_start_end_simul. \
            call_async(backend_node.start_end_simul_srv)
        reporting_start_simul, tout_start_simul = wait_future(backend_node, future_start_simul)

        future_waypoints = backend_node.client_waypoints. \
            call_async(backend_node.waypoints_srv)
        reporting_waypoints, tout_waypoints = wait_future(backend_node, future_waypoints)

        if tout_start_simul or tout_waypoints:
            backend_node.get_logger().info('returning HTTP Gateaway timedout to client')
            return json.dumps({'success':False}), 504, {'ContentType':'application/json'}
        else:
            backend_node.get_logger().info("Received reporting: %s" % reporting_start_simul)
            backend_node.get_logger().info("Received reporting: %s" % reporting_waypoints)
            backend_node.get_logger().info('returning HTTP OK to client')
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info('returning HTTP internal server error to client')
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

@app.route("/end")
def end_simul():
    try:
        backend_node.start_end_simul_srv.end_simul = True

        backend_node.get_logger().info("Ending system")

        future_end_simul = backend_node.client_start_end_simul. \
            call_async(backend_node.start_end_simul_srv)
        reporting_end_simul, tout_end_simul = wait_future(backend_node, future_end_simul)

        if tout_end_simul:
            backend_node.get_logger().info('returning HTTP Gateaway timedout to client')
            return json.dumps({'success':False}), 504, {'ContentType':'application/json'}
        else:
            backend_node.get_logger().info("Received reporting: %s" % reporting_end_simul)
            backend_node.get_logger().info('returning HTTP OK to client')
            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}
    except:
        backend_node.get_logger().info('returning HTTP internal server error to client')
        return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

def main():
    try:
        app.run() # port 5000 by default
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    finally:
        backend_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()



