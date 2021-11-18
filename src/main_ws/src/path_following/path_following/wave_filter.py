import sys
import os
import glob
import traceback

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.signal import sosfreqz
 
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

        #considering wn = [0.4, 0.63, 1]
        self.num = np.array([1, 2.842, 4.07, 3.277, 1.623, 0.4523, 0.0635])
        self.den = np.array([1, 4.06, 6.685, 5.709, 2.667, 0.6461, 0.0635])

        #considering wn = [0.52124 - 0.23, 0.52124, 0.52124 + 0.37]
        #self.num = np.array([1, 2.385, 2.868, 1.892, 0.758, 0.1659, 0.0183])
        #self.den = np.array([1, 3.407, 4.655, 3.255, 1.228, 0.237, 0.0183])

        # obs: low pass at 10Hz (like Fossen) is not even possible because the state is
        # sampled at 10Hz (can only work with <5Hz)
        # Fossen's 3 2order cascades: [0.4rad/s, 0.63rad/s, 1rad/s])
        # [0.4rad/s, 0.63rad/s, 1rad/s]) == [0.063Hz, 0.100Hz, 0.159Hz])
        # p23 wave period is 12 seconds -> freq is 0.08333333333 Hz

        ########### <pedro> ################
        # soh vai mudar o lado direito dessa linha aqui!!(comenta a linha em vez de apagar)
        # o output seu vai ser do tipo (z,p,k). 
        # Usar a funcao zpk2sos(z,p,k) que converte pra sos (tipo que esta feito abaixo)

        self.z, self.p, self.k = signal.tf2zpk(self.num, self.den)

        self.z2, self.p2, self.k2 = signal.bilinear_zpk(self.z, self.p, self.k, 10)

        # wave is at 0.083 Hz or 0.52124 rad/s which is inside the band, but in the edge 
        # exact fossens frequencies
        # self.sos = signal.butter(6, [0.063, 0.159], 'bandstop', fs=10, output='sos')
        # centralized on our wave frequency (fossen's but shifted)
        self.sos = signal.butter(6, [0.046352285679, 0.14184525164], 'bandstop', fs=10, output='sos') 

        ##################### <pedro/> ##############

        #sos from bilinear filter signal
        self.sos_notch_fossen = signal.zpk2sos(self.z2, self.p2, self.k2)
        self.zi3 = signal.sosfilt_zi(self.sos_notch_fossen)

        self.zi = signal.sosfilt_zi(self.sos)

        # # chosen 0.3 by testing some values in this range
        self.sos2 =  signal.butter(6, 0.3, fs=10, output='sos')
        self.zi2 = signal.sosfilt_zi(self.sos2)

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

    def callback_shutdown(self, _):
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
        # band stop (notch): remove wave component
        state_history_filtered = map(lambda sig: signal.sosfilt(self.sos, sig, zi=sig[0]*self.zi)[0], self.simulated_state_history)
        # low pass: remove high freq noise from white noise added by gps_imu_simul
        # comment line below when gps_imu_simul is not activated
        # state_history_filtered = map(lambda sig: signal.sosfilt(self.sos2, sig, zi=sig[0]*self.zi2)[0], state_history_filtered)
        # state_history_filtered = map(lambda sig: signal.sosfilt(self.sos_notch_fossen, sig, zi=sig[0]*self.zi3)[0], state_history_filtered)
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

        t = self.TIME_STEP*np.array(range(len(self.filtered_state_history[0])))
        fs_dir = "filteredState"
        filtered_state_props = [
            {
                "title": "Filtered Linear Position X",
                "ylabel": "x [m]",
                "file": "filteredLinearPositionX.png"
            },
            {
                "title": "Filtered Linear Position Y",
                "ylabel": "y [m]",
                "file": "filteredLinearPositionY.png"
            },
            {
                "title": "Filtered Angular Position Theta",
                "ylabel": r"$\theta\;[rad\;(from\;east\;counterclockwise)]$",
                "file": "filteredAngularPositionTheta.png"
            },
            {
                "title": "Filtered Linear Velocity U",
                "ylabel": "u [m/s]",
                "file": "filteredLinearVelocityU.png"
            },
            {
                "title": "Filtered Linear Position V",
                "ylabel": "v [m/s (port)]",
                "file": "filteredLinearVelocityV.png"
            },
            {
                "title": "Filtered Angular Velocity R",
                "ylabel": "r [rad/s (counterclockwise)]",
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
        
        bode_dir = "bodePlots"

        filters = [
            {
                'dtf': self.sos3,
                'title': 'Wave filter - Frequency response',
                'file': 'notchFilterBodePlot.png'
            },
            {
                'dtf': self.sos2,
                'title': 'Sensor noise filter - Frequency response',
                'file': 'lowPassFilterBodePlot.png'
            }
        ]

        #clean before
        files = glob.glob(os.path.join(self.plots_dir, bode_dir, '*.png'))
        for f in files:
            os.remove(f)

        for filter in filters:
            # Bode plot
            fig, ax = plt.subplots(2)
            fig.suptitle(filter['title'], fontsize=16)
            w, h = sosfreqz(filter['dtf'], worN=8000, fs=10)

            ## Gain
            axGain = ax[0]
            db = 20*np.log10(np.maximum(np.abs(h), 1e-5))
            axGain.semilogx(w, db)
            axGain.set_title('Gain')
            axGain.set_ylim(min(db), max(db))
            axGain.axes.get_xaxis().set_visible(False)
            axGain.set_ylabel("Gain [dB]")                          

            ## Phase
            axPhase = ax[1]
            negative_phase = [(-phase - 180) if phase > 0 else phase for phase in np.rad2deg(np.angle(h))]
            axPhase.semilogx(w, negative_phase)
            axPhase.set_title('Phase')
            axPhase.set_ylim(min(negative_phase), 0)
            axPhase.set_xlabel("Frequency [Hz]")
            axPhase.set_ylabel("Phase [deg]")

            fig.savefig(os.path.join(self.plots_dir, bode_dir, filter['file']))

def main(args=None):
    try:
        rclpy.init(args=args)
        wave_filter_node = WaveFilter()
        rclpy.spin(wave_filter_node)
    except KeyboardInterrupt:
        print('Stopped with user interrupt')
        wave_filter_node.get_logger().info('Stopped with user interrupt')
    except SystemExit:
        pass
    except:
        print(traceback.format_exc())
    finally:
        wave_filter_node.generate_plots()
        wave_filter_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()