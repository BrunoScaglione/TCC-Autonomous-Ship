import sys
import collections

import matplotlib.pyplot as plt

from scipy import signal
 
import rclpy
from rclpy.node import Node

from std_msgs.msg import Bool
# custom interface
from path_following_interfaces.msg import State

class WaveFilter(Node):
    def __init__(self):
        super().__init__('wave_filter_node')

        # debugging
        self.u_history = []
        self.u_filtered_history = []
        self.theta_history = []
        self.theta_filtered_history = []
        self.y_history = []
        self.y_filtered_history = []

        # obs: low pass at 10Hz (like Fossen) is not even possible because the state is
        # sampled at 10Hz (can only work with <5Hz)
        # aproximating Fossen's 3 2order cascades at [0.4rad/s, 0.63rad/s, 1rad/s]) didnt work (large bias)
        # p23 wave period is 4 seconds -> freq is 0.25 Hz
        self.sos = signal.butter(6, [0.24, 0.26], 'bandstop', fs=10, output='sos')
        self.zi = signal.sosfilt_zi(self.sos)

        # for 6 order filter
        # TODO: hardcoded now, but needs to recceive from initial condition
        self.last_seven_states = collections.deque([], maxlen=7) 

        self.xf_msg = State()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_estimated_state = self.create_subscription(
            State,
            '/estimated_state',
            self.callback_estimated_state,
            1)

        self.publisher_filtered_state = self.create_publisher(
            State,
            '/filtered_state',
            1)

    def callback_shutdown():
        sys.exit()
        
    def callback_estimated_state(self, msg):
        self.log_state(msg, 'subscriber')
        self.last_seven_states.append(msg)
        self.u_history.append(msg.velocity.u) # debugging
        self.theta_history.append(msg.position.theta) # debugging
        self.y_history.append(msg.position.y) # debugging
        filtered_state_msg = self.state_filter(msg)
        self.publisher_filtered_state.publish(filtered_state_msg)
        self.log_state(filtered_state_msg, 'publisher')
    
    def state_filter(self, x):
        # filters entire state
        # debugging

        x_last_seven = [state.position.x for state in list(self.last_seven_states)]
        y_last_seven = [state.position.y for state in list(self.last_seven_states)]
        theta_last_seven = [state.position.theta for state in list(self.last_seven_states)]
        u_last_seven = [state.velocity.u for state in list(self.last_seven_states)]
        v_last_seven = [state.velocity.v for state in list(self.last_seven_states)]
        r_last_seven = [state.velocity.r for state in list(self.last_seven_states)]
        state_last_seven = [
            x_last_seven, 
            y_last_seven, 
            theta_last_seven, 
            u_last_seven, 
            v_last_seven,
            r_last_seven
        ]

        state_last_seven_filtered = map(lambda sig: signal.sosfilt(self.sos, sig, zi=sig[0]*self.zi)[0], state_last_seven)
        state_current_filtered = [sig[-1] for sig in state_last_seven_filtered]
        self.xf_msg.position.x = state_current_filtered[0]
        self.xf_msg.position.y = state_current_filtered[1]
        self.y_filtered_history.append(self.xf_msg.position.y) # debugging
        self.xf_msg.position.theta = state_current_filtered[2]
        self.theta_filtered_history.append(self.xf_msg.position.theta) # debugging


        self.xf_msg.velocity.u = state_current_filtered[3]
        self.u_filtered_history.append(self.xf_msg.velocity.u) # debugging
        self.xf_msg.velocity.v = state_current_filtered[4]
        self.xf_msg.velocity.r = state_current_filtered[5]

        self.xf_msg.time = x.time

        return self.xf_msg


    def log_state(self, state, communicator):
        log_str = 'listened estimated' if communicator == 'subscriber' else 'published filtered'
        self.get_logger().info(
            '%s state: {position: {x: %f, y: %f, theta: %f}, velocity: {u: %f, v: %f, r: %f}, time: %f}' 
            % (
                log_str,
                state.position.x, 
                state.position.y, 
                state.position.theta, # yaw angle
                state.velocity.u, 
                state.velocity.v, 
                state.velocity.r,
                state.time 
            )
        )

def main(args=None):
    try:
        rclpy.init(args=args)
        wave_filter_node = WaveFilter()
        rclpy.spin(wave_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        plt.plot(wave_filter_node.u_history) # debugging
        plt.plot(wave_filter_node.u_filtered_history) # debugging
        plt.plot(wave_filter_node.theta_history) # debugging
        plt.plot(wave_filter_node.theta_filtered_history) # debugging
        plt.legend([
            "Real surge velocity", 
            "Filtered surge velocity",
            "Real yaw angle", 
            "Filtered yaw angle"
        ]) # debugging
        plt.show()
        plt.plot(wave_filter_node.y_history) # debugging
        plt.plot(wave_filter_node.y_filtered_history) # debugging
        plt.legend([
            "Real y",
            "Filtered y"
        ]) # debugging
        plt.show() # debugging
    except SystemExit:
        print('Stopped with user shutdown request')
    except Exception as e:
        print(e)
    finally:
        wave_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()