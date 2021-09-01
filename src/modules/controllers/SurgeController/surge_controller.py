import math

import modules.controllers.SurgeController as SurgeController

phi = SurgeController.phi
xd = SurgeController.xd

def getNp(tau: float, x:float) -> float:
    c1 = 0.0354
    c2 = 3.8107
    c3 = -0.0691 
    return c1*math.sqrt(c2*(x**2) + tau) - c3*x

def controller(x: float) -> float:
    # sliping variable
    s = x - xd
    # sat function
    sats = max(-1,min(s/phi,1))
    # input as function of x (control)
    u = x*abs(x)*(1.9091*(10**-4) + 5.2142*(10**-5)*sats)
    # thrust
    tau = u*(m - X_added_mass)
    # control allocation
    Np = getNp(u, x)

    return [s, tau, Np] 