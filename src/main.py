from modules.simulation import simulation
from modules.controllers.SurgeController.utils.plots import getPlots as surge_plots
from modules.controllers.SurgeController.utils.metrics import getMetrics as surge_metrics

def main():
    # simulation results
    vets = simulation()
    # plot results
    surge_plots(*vets)
    # get metrics from results
    sm = surge_metrics(*vets)
    print(sm)

if __name__ == "__main__":
    main()