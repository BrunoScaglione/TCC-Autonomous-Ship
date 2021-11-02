import matplotlib.pyplot as plt
import numpy as np

import modules.controllers.SurgeController as SurgeController 

def getPlots(
    tspan: np.array, 
    vetx: np.array, 
    vets: np.array, 
    vettau: np.array,
    vetnp: np.array,
    vetyaw: np.array,
    vetangle: np.array,
    vetspeed: np.array
    ):

    params = {'mathtext.default': 'regular'}
    plt.rcParams.update(params)

    fig, axs = plt.subplots(3)
    #fig.suptitle("Surge velocity, sliding variable, thrust, and rotation\n from top to bottom; through time")
    
    axs[0].plot(tspan, vetyaw)
    axs[0].set_ylabel(r"dem rudder angle")
    axs[0].axes.get_xaxis().set_visible(False)
    axs[2].set_ylim([-1,1])

    axs[1].plot(tspan, vetangle)
    axs[1].set_ylabel(r"$\psi$")
    axs[1].axes.get_xaxis().set_visible(False)
    axs[2].set_ylim([-3,3])
    
    axs[2].plot(tspan, vetspeed)
    axs[2].set_ylabel(r"r")
    axs[2].set_xlabel(r"$t [s]$")
    axs[2].set_ylim([-0.01,0.01])
    
    """axs[0].plot(tspan, vetx)
    axs[0].set_ylabel(r"$u [m/s]$")
    axs[0].axes.get_xaxis().set_visible(False)
    axs[3].set_ylim([0,5])

    axs[1].plot(tspan, vets)
    axs[1].set_ylabel(r"$s$")
    axs[1].axes.get_xaxis().set_visible(False)
    axs[3].set_ylim([-5,0])

    axs[2].plot(tspan, vettau)
    axs[2].set_ylabel(r"$\tau_1 [kN]$")
    axs[2].axes.get_xaxis().set_visible(False)
    axs[3].set_ylim([0,2363])
	
    axs[3].plot(tspan, vetnp)
    axs[3].set_ylabel(r"$n_p [Hz]$")
    axs[3].set_xlabel(r"$t [s]$")
    axs[3].set_ylim([0,1.75])"""

    graphics_file = "simulation.png" \
    if (SurgeController.K > 1) and (SurgeController.kphi > 1) else "simulation_raw.png"

    plt.savefig("modules/controllers/SurgeController/results/" + graphics_file)
    #plt.show()
    