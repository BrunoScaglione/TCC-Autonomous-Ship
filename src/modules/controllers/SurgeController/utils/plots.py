import matplotlib.pyplot as plt
import numpy as np

def getPlots(
    tspan: np.array, 
    vetx: np.array, 
    vets: np.array, 
    vettau: np.array,
    vetnp: np.array):

    params = {'mathtext.default': 'regular'}
    plt.rcParams.update(params)

    fig, axs = plt.subplots(4)
    fig.suptitle("Surge velocity, sliding variable, thrust, and rotation from top to bottom; through time")
    axs[0].plot(tspan, vetx)
    axs[0].set_ylabel("$u [m/s]$")

    axs[1].plot(tspan, vets)
    axs[1].set_ylabel("$s$")

    axs[2].plot(tspan, vettau)
    axs[2].set_ylabel("$\tau_1 [kN]$")
	
    axs[3].plot(tspan, vetnp)
    axs[3].set_ylabel("$n_p [Hz]$")
    axs[3].set_xlabel("$t [s]$")

    plt.savefig("modules/controllers/SurgeController/results/simulation.png")