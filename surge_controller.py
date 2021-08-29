import pydyna
import math
import matplotlib.pyplot as plt
import numpy as np

def getplots():
    fig, axs = plt.subplots(2)
    fig.suptitle('Surge velocity (1) and control input (2), through time')
    axs[0].plot(tspan, vetx)
    axs[0].ylabel ("u [m/s]")
	
    axs[1].plot(tspan, vetu)
    axs[1].ylabel ("n_p [Hz]")
    axs[1].xlabel ("t [s]")

# converts trust force to rotation
def getnp(tau: float, x:float) -> int:
    c1 = 0.0354
    c2 = 3.8107
    c3 = -0.0691 
    return c1*sqrt(c2*(x**2) + tau) - c3*x

def main():
    print('Starting...')

    try:
        xd = 5 # desired surge velocity
        sim = pydyna.create_simulation('./TankerL186B32_T085.p3d')
        ship = sim.vessels['0']
        propeller = ship.thrusters['0']

        dt = 0.1 # p3d file
        t_end = 1000
        steps = t_end/dt + 1

        # saturation parameter, 
        # width of boundary layer or 
        # steady-state error upper bound
        phi = 0.01

        vetx = np.zeros((steps))
        vetu = np.zeros((steps))

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
            # control allocation
            np = getnp(u, x)
            propeller.dem_rotation = np

            # save history
            vetx[i] = x
            vetu[i] = u

            # next step
            sim.step()

        
        tspan = np.arange(0,t_end,dt)
        # plot u vs t (x vs t) and np vs t (u vs t)
        getplots()
    except:
        print('Error loading simulation!')
        raise

if __name__ == "__main__":
    main()
        