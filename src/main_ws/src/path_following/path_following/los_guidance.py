#first will receive waypoints from backend within a service
# then will receive filtered state and publish desired yaw angle and desired velocity 
# (or we just use fixed velocity)

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
#custom service
from path_following_interfaces.srv import Waypoints

class LosGuidance(Node):
    def __init__(self):
        super().__init__('los_guidance_node')

        self.current_waypoint = 1 #index of waypoint ship has to reach (includes starting (0,0,0)

        self.server = self.create_service(Waypoints, '/waypoints', self.callback_waypoints)

        self.subscription_filtered_state = self.create_subscription(
            State,
            '/filtered_state',
            self.callback_filtered_state,
            1)

        self.publisher_desired_yaw_angle = self.create_publisher(
            Float32,
            '/desired_yaw_angle',
            1)

    def log_state(self, msg):
        self.get_logger().info(
            'listened filtered state: {position: {x: %f, y: %f, psi: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
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

    def callback_waypoints(self, req, res):
        self.waypoints = req # {position: {x: , y: } velocity: }
        num_waypoints = len(req.position.x)
        self.get_logger().info('listened %d waypoints' % num_waypoints)
        for i in range(num_waypoints):
            self.get_logger().info('listened waypoint %d: %f %f %f' % (i, req.position.x[i], req.position.y[i], req.velocity[i]))
        res.reporting = 'Received Waypoints'
        return res
        
    def callback_filtered_state(self, msg):
        log_state(self, msg)
        des_yaw_msg, des_velocity_msg = self.los(msg)
        self.publisher_desired_yaw_angle.publish(des_yaw_msg)
        self.get_logger().info('published desired yaw angle: %f' % des_yaw_msg.data)
        self.publisher_desired_surge_velocity.publish(des_velocity_msg)
        self.get_logger().info('published desired velocity: %f' % des_velocity_msg.data)
    
    def los(self, filtered_state):
        # use waypoints stored in self.waypoints
        # these contain desired position x and y, and velocity u
        des_yaw_msg = Float32()
        des_velocity_msg = Float32()
        des_yaw_msg.data = 1
        des_velocity_msg.data = 1 
        return des_yaw_msg, des_velocity_msg

def main(args=None):
    rclpy.init(args=args)
    los_guidance_node = LosGuidance()
    
    rclpy.spin(los_guidance_node)

    los_guidance_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()