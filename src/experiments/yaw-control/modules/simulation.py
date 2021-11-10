import pydyna
import numpy as np

from modules.controllers.SurgeController import surge_controller
from modules.controllers.SurgeController import yawcontroller

def simulation():
    print('Starting...')

    try:
        sim = pydyna.create_simulation('./config/TankerL186B32_T085.p3d')
        ship = sim.vessels['104']
        propeller = ship.thrusters['0']
        rudder = ship.rudders['0']

        #simulation parameters
        dt = 0.1 # p3d file
        t_end = 1000
        steps = int(t_end/dt)
        
        
        # initialize 
        vetx = np.zeros((steps))
        vets = np.zeros((steps))
        vettau = np.zeros((steps))
        vetnp = np.zeros((steps))
        vetyaw = np.zeros((steps))
        vetangle = np.zeros((steps))
        vetspeed = np.zeros((steps))
        counter = 0 

        for i in range(0, steps):
            #print(f'Step: {i}')

            # surge velocity (part of the state)
            x = ship.linear_velocity[0]
            psi = ship.angular_position[2]
            r = ship.angular_velocity[2]
            s, tau, Np = surge_controller.controller(x)
            yaw, soma = yawcontroller.controller(counter, r, psi)
            propeller.dem_rotation = Np
            rudder.dem_angle = yaw

            # save history
            vetx[i] = x
            vets[i] = s
            vettau[i] = tau
            vetnp[i] = Np
            vetyaw[i] = yaw
            vetangle[i] = psi
            vetspeed[i] = r
            
            
            counter = soma

            sim.step()

        tspan = np.linspace(0,t_end,steps)
        print("heading angle", psi)
        print("soma erro", counter)
        # plot u vs t (x vs t) and np vs t (u vs t)
        return [tspan, vetx, vets, vettau, vetnp, vetyaw, vetangle, vetspeed]
    except:
        print('Error loading simulation!')
        raise