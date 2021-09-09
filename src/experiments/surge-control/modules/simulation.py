import pydyna
import numpy as np

from modules.controllers.SurgeController import surge_controller

def simulation():
    print('Starting...')

    try:
        sim = pydyna.create_simulation('./config/TankerL186B32_T085.p3d')
        ship = sim.vessels['104']
        propeller = ship.thrusters['0']

        #simulation parameters
        dt = 0.1 # p3d file
        t_end = 1000
        steps = int(t_end/dt)

        # initialize 
        vetx = np.zeros((steps))
        vets = np.zeros((steps))
        vettau = np.zeros((steps))
        vetnp = np.zeros((steps))

        for i in range(0, steps):
            #print(f'Step: {i}')

            # surge velocity (part of the state)
            x = ship.linear_velocity[0]
            s, tau, Np = surge_controller.controller(x)
            propeller.dem_rotation = Np

            # save history
            vetx[i] = x
            vets[i] = s
            vettau[i] = tau
            vetnp[i] = Np

            # if Np > 1.7:
            #     print(f"x = {x}")
            #     print(f"tau = {tau}")
            #     print(f"Np = {Np}")

            # next step
            sim.step()

        tspan = np.linspace(0,t_end,steps)
        # plot u vs t (x vs t) and np vs t (u vs t)
        return [tspan, vetx, vets, vettau, vetnp]
    except:
        print('Error loading simulation!')
        raise