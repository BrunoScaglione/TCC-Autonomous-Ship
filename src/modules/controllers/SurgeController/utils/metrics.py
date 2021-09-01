import math
import numpy as np

import modules.controllers.SurgeController as SurgeController       

x0 = SurgeController.x0
xd = SurgeController.xd
phi = SurgeController.phi

def getMetrics(
    tspan: np.array, 
    vetx: np.array, 
    vets: np.array, 
    vettau: np.array,
    vetnp: np.array) -> dict:

    idx_ts = np.where(vetx>0.02*(x0-(xd-phi))+(xd-phi))[0]
    print(f"idx_ts = {idx_ts}")
    ts = tspan[idx_ts];
    print(f"ts = {ts}")
    idx_ta = np.where(vets> -phi)[0];
    print(f"idx_ta = {idx_ta}")
    ta = tspan[idx_ta];
    print(f"ta = {ta}")

    overshoot = max(vetx) - xd
    print(f"overshoot = {overshoot}")

    e_regime = vetx[-1]-xd;
    print(f"e_regime = {e_regime}")

    x_slipstart = vetx[idx_ta];
    print(f"x_slipstart = {x_slipstart}")
    x_tau = x_slipstart + 0.6321*(xd-x_slipstart);
    print(f"x_tau = {x_tau}")
    idx_tau = np.where(vetx>x_tau)[0];
    print(f"idx_tau = {idx_tau}")
    tau = tspan[idx_tau] - tspan[idx_ta];
    print(f"tau = {tau}")

    tau_max = max(vettau)
    print(f"tau_max = {tau_max}")
    np_max = max(vetnp)
    print(f"np_max = {np_max}")

    metrics = {
        "ts": ts,
        "ta": ta,
        'e': e,
        "overshoot": overshoot,
        "tau_max": tau_max,
        "np_max": np_max
    }

    return metrics