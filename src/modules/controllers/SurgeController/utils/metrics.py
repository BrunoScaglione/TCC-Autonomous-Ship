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