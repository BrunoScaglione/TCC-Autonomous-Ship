import json

from modules.simulation import simulation
from modules.controllers.SurgeController.utils.plots import getPlots as surge_plots
from modules.controllers.SurgeController.utils.metrics import getMetrics as surge_metrics

import modules.controllers.SurgeController as SurgeController

kf = SurgeController.kf
kphi = SurgeController.kphi

def main():
    # simulation results
    vets = simulation()
    # plot results
    surge_plots(*vets)
    # get metrics from results
    params = f"for kf = {kf} and kphi = {kphi}\n"
    print(params)
    sm = surge_metrics(*vets)
    metrics = json.dumps(sm) + '\n'
    print(metrics)

    with open("modules/controllers/SurgeController/results/logs.txt",'a') as writer:
        writer.write(params)
        writer.write(metrics)

if __name__ == "__main__":
    main()