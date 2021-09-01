from modules.simulation import simulation
import modules.controllers.SurgeController as SurgeController

def main():
    # simulation results
    vets = simulation()
    # plot results
    SurgeController.surge_plots(*vets)
    # get metrics from results
    SurgeController.surge_metrics(*vets)
    print(surge_metrics)

if __name__ == "__main__":
    main()