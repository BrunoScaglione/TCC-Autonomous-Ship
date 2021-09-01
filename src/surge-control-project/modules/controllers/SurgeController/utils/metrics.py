import math
import numpy as np

import modules.controllers.SurgeController as SurgeController       

x0 = SurgeController.x0
xd = SurgeController.xd
kphi = SurgeController.kphi
phi = SurgeController.phi
phi = kphi*phi

def getMetrics(
    tspan: np.array, 
    vetx: np.array, 
    vets: np.array, 
    vettau: np.array,
    vetnp: np.array) -> dict:

    idx_ts = np.where(vetx>0.02*(x0-(xd-phi))+(xd-phi))[0][0] 
    ts = tspan[idx_ts];
    idx_tr = np.where(vets> -phi)[0][0];
    tr = tspan[idx_tr];

    overshoot = max(vetx) - xd

    e = vetx[-1]-xd;

    x_slipstart = vetx[idx_tr];
    x_tau = x_slipstart + 0.6321*(xd-x_slipstart);
    idx_tau = np.where(vetx>x_tau)[0];
    tau = tspan[idx_tau] - tspan[idx_tr];

    tau_max = max(vettau)
    np_max = max(vetnp)

    metrics = {
        "ts": ts,
        "tr": tr,
        'e': e,
        "overshoot": overshoot,
        "tau_max": tau_max,
        "np_max": np_max
    }

    return metrics