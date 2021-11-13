import sys
import os
import glob

import traceback

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

        self.TIME_STEP = 0.1

        self.declare_parameter('plots_dir', './')
        self.plots_dir = self.get_parameter('plots_dir').get_parameter_value().string_value

        self.filtered_state_history = [[],[],[],[],[],[]]
        self.simulated_state_history = [[],[],[],[],[],[]]


        # obs: low pass at 10Hz (like Fossen) is not even possible because the state is
        # sampled at 10Hz (can only work with <5Hz)
        # aproximating Fossen's 3 2order cascades at [0.4rad/s, 0.63rad/s, 1rad/s]) didnt work (large bias)
        # p23 wave period is 4 seconds -> freq is 0.25 Hz
        # self.sos = signal.butter(6, [0.2, 0.3], 'bandstop', fs=10, output='sos')
        self.sos = signal.butter(6, 0.2, fs=10, output='sos')
        self.zi = signal.sosfilt_zi(self.sos)
        # self.sos2 = signal.butter(6, [0.016, 0.025], 'bandstop', fs=10, output='sos')
        # self.zi2 = signal.sosfilt_zi(self.sos2)

        self.xf_msg = State()

        self.subscription_shutdown = self.create_subscription(
            Bool,
            '/shutdown',
            self.callback_shutdown,
            1)

        self.subscription_simulated_state = self.create_subscription(
            State,
            '/simulated_state',
            self.callback_simulated_state,
            1)

        self.publisher_filtered_state = self.create_publisher(
            State,
            '/filtered_state',
            1)

    def callback_shutdown(self):
        self.get_logger().info('User requested total shutdown')
        sys.exit()
        
    def callback_simulated_state(self, msg):
        self.log_state(msg, 'subscriber')

        self.simulated_state_history[0].append(msg.position.x)
        self.simulated_state_history[1].append(msg.position.y)
        self.simulated_state_history[2].append(msg.position.theta)
        self.simulated_state_history[3].append(msg.velocity.u)
        self.simulated_state_history[4].append(msg.velocity.v)
        self.simulated_state_history[5].append(msg.velocity.r)

        filtered_state_msg = self.state_filter(msg.time)
        self.publisher_filtered_state.publish(filtered_state_msg)
        self.log_state(filtered_state_msg, 'publisher')
    
    def state_filter(self, t):
        # filters entire state
        state_history_filtered = map(lambda sig: signal.sosfilt(self.sos, sig, zi=sig[0]*self.zi)[0], self.simulated_state_history)
        # state_history_filtered = map(lambda sig: signal.sosfilt(self.sos2, sig, zi=sig[0]*self.zi2)[0], state_history_filtered)
        state_current_filtered = [sig[-1] for sig in state_history_filtered]

        self.xf_msg.position.x = state_current_filtered[0]
        self.xf_msg.position.y = state_current_filtered[1]
        self.xf_msg.position.theta = state_current_filtered[2]
        self.xf_msg.velocity.u = state_current_filtered[3]
        self.xf_msg.velocity.v = state_current_filtered[4]
        self.xf_msg.velocity.r = state_current_filtered[5]
        self.xf_msg.time = t

        self.filtered_state_history[0].append(self.xf_msg.position.x)
        self.filtered_state_history[1].append(self.xf_msg.position.y)
        self.filtered_state_history[2].append(self.xf_msg.position.theta)
        self.filtered_state_history[3].append(self.xf_msg.velocity.u)
        self.filtered_state_history[4].append(self.xf_msg.velocity.v)
        self.filtered_state_history[5].append(self.xf_msg.velocity.r)

        return self.xf_msg


    def log_state(self, state, communicator):
        log_str = 'listened simulated' if communicator == 'subscriber' else 'published filtered'
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

    def generate_plots(self):
        #clean before
        files = glob.glob(os.path.join(self.plots_dir, 'simulatedState', '*.png'))
        for f in files:
            os.remove(f)

        params = {'mathtext.default': 'regular'}
        plt.rcParams.update(params)

        t = [self.TIME_STEP*i for i in range(len(self.filtered_state_history[0]))]
        fs_dir = "filteredState"
        filtered_state_props = [
            {
                "title": "Filtered Linear Position X",
                "ylabel": r"$x\;[m]$",
                "file": "filteredLinearPositionX.png"
            },
            {
                "title": "Filtered Linear Position Y",
                "ylabel": r"$y\;[m]$",
                "file": "filteredLinearPositionY.png"
            },
            {
                "title": "Filtered Angular Position Theta",
                "ylabel": r"$\theta\;[rad\;(from\;east\;counterclockwise)]$",
                "file": "filteredAngularPositionTheta.png"
            },
            {
                "title": "Filtered Linear Velocity U",
                "ylabel": r"$u\;[m/s]$",
                "file": "filteredLinearVelocityU.png"
            },
            {
                "title": "Filtered Linear Position V",
                "ylabel": r"$v\;[m/s\;(port)]$",
                "file": "filteredLinearVelocityV.png"
            },
            {
                "title": "Filtered Angular Velocity R",
                "ylabel": r"$r\;[rad/s (counterclockwise)]$",
                "file": "filteredAngularVelocityR.png"
            },
        ]

        for i in range(len(self.filtered_state_history)):
            fig, ax = plt.subplots(1)
            ax.set_title(filtered_state_props[i]["title"])
            ax.plot(t, self.filtered_state_history[i])
            ax.set_xlabel(r"$t\;[s]$")
            ax.set_ylabel(filtered_state_props[i]["ylabel"])
            ax.set_ylim([min(self.filtered_state_history[i]), max(self.filtered_state_history[i])])

            fig.savefig(os.path.join(self.plots_dir, fs_dir, filtered_state_props[i]["file"]))

def main(args=None):
    try:
        rclpy.init(args=args)
        wave_filter_node = WaveFilter()
        rclpy.spin(wave_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
    except SystemExit:
        print('Stopped with user shutdown request')
    except:
        print(traceback.format_exc())
    finally:
        wave_filter_node.generate_plots()
        wave_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()