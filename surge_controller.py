import pydyna
import math
import matplotlib.pyplot as plt
import numpy as np

plt.rc('text', usetex=True)

def getPlots():
    fig, axs = plt.subplots(4)
    fig.suptitle(r"Surge velocity, sliding variable, thrust, and rotation from top to bottom; through time")
    axs[0].plot(tspan, vetx)
    axs[0].ylabel(r"u [m/s]")

    axs[1].plot(tspan, vets)
    axs[1].ylabel(r"s")

    axs[2].plot(tspan, vettau)
    axs[2].ylabel(r"\tau_1 [kN]")
	
    axs[3].plot(tspan, vetnp)
    axs[3].ylabel(r"n_p [Hz]")
    axs[3].xlabel(r"t [s]")

    plt.savefig("results/pydyna_surge_control.png")

def getMetrics(tspan, vetx, vets, vettau, vetnp):
    idx_ts = numpy.where(vetx>0.02*(x0-(xd-phi))+(xd-phi))[0]
    ts = tspan[idx_ts];

    idx_ta = np.where(vets> -phi)[0];
    ta = tspan[idx_ta];

    overshoot = max(vetx) - xd

    e_regime = vetx[-1]-xd;

    x_slipstart = vetx[idx_ta];
    x_tau = x_slipstart + 0.6321*(xd-x_slipstart);
    idx_tau = np.where(vetx>x_tau)[0];
    tau = tspan[idx_tau] - tspan[idx_ta];

    tau_max = max(vettau)
    np_max = max(vetnp)

    metrics = {
        "ts": ts,
        "ta": ta,
        'e': e,
        "overshoot": overshoot,
        "tau_max": tau_max,
        "np_max": np_max
    }

    return metrics


# converts trust force to rotation
def getNp(tau: float, x:float) -> int:
    c1 = 0.0354
    c2 = 3.8107
    c3 = -0.0691 
    return c1*sqrt(c2*(x**2) + tau) - c3*x

def main():
    print('Starting...')

    try:
        sim = pydyna.create_simulation('config/TankerL186B32_T085.p3d')
        ship = sim.vessels['0']
        propeller = ship.thrusters['0']

        dt = 0.1 # p3d file
        t_end = 1000
        steps = t_end/dt + 1

        phi = 0.01 # steady-state error upper bound
        xd = 5 # desired surge velocity
        m = 40415
        X_added_mass = -3375
        x0 = 0

        vetx = np.zeros((steps))
        vets = np.zeros((steps))
        vetu = np.zeros((steps))
        vetnp = np.zeros((steps))

        for i in range(0, steps):
            print(f'Step: {i}')

            # surge velocity (part of the state)
            x = ship.linear_velocity[0]
            # sliping variable
            s = x - xd
            # sat function
            sats = max(-1,min(s/phi,1))
            # input as function of x (control)
            u = x*abs(x)*(1.9091*(10**-4) + 5.2142*(10**-5)*sats)
            # thrust
            tau = u*(m - X_added_mass)
            # control allocation
            np = getNp(u, x)
            propeller.dem_rotation = np

            # save history
            vetx[i] = x
            vets[i] = s
            vettau[i] = tau
            vetnp[i] = np

            # next step
            sim.step()

        
        tspan = np.arange(0,t_end,dt)
        # plot u vs t (x vs t) and np vs t (u vs t)
        getPlots()
        metrics = getMetrics()
        print(metrics)
    except:
        print('Error loading simulation!')
        raise

if __name__ == "__main__":
    main()
        