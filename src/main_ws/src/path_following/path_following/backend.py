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
        while true:
            rclpy.spin_once(node)
            if node_future.done():
                try:
                    return node_future.result()
                except Exception as e:
                    node.get_logger().info("Service call failed %r" % (e,))
                    return None

app = Flask(__name__)

@app.route("/waypoints", methods=['POST'])
def receive_waypoints():
    waypoints = request.json

    backend_node.waypoints_srv.position.x = waypoints['position']['x']
    backend_node.waypoints_srv.position.y = waypoints['position']['y']
    backend_node.waypoints_srv.velocity = waypoints['velocity']

@app.route("/inital_condition", methods=['POST'])
def receive_inital_condition():
    initial_condition = request.json

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

@app.route("/start")
def start_system():
    backend_node.start_end_simul_srv.end_simul = 0

    future_start_simul = backend_node.client_start_end_simul. \
        call_async(backend_node.start_end_simul_srv)
    reporting_start_simul = backend_node.wait_future(backend_node, future_start_simul)
    backend_node.get_logger().info("Received reporting: %s" % reporting_start_simul)

    future_waypoints = backend_node.client_waypoints. \
        call_async(backend_node.waypoints_srv)
    reporting_waypoints = backend_node.wait_future(backend_node, future_waypoints)
    backend_node.get_logger().info("Received reporting: %s" % reporting_waypoints)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route("/end")
def end_simul():
    backend_node.start_end_simul_srv.end_simul = 1
    future_end_simul = backend_node.client_start_end_simul. \
        call_async(backend_node.start_end_simul_srv)
    reporting_end_simul = backend_node.wait_future(backend_node, future_end_simul)
    backend_node.get_logger().info("Received reporting: %s" % reporting_end_simul)
    
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

if __name__ == '__main__':
    app.run() # port 5000 by default



