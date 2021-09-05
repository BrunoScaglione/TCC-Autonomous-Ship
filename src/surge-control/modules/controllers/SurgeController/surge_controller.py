import math

import modules.controllers.SurgeController as SurgeController

kphi = SurgeController.kphi
phi = SurgeController.phi
phi = kphi*phi
xd = SurgeController.xd
m = SurgeController.m
X_added_mass = SurgeController.X_added_mass
# gain: tuning parameter
K = SurgeController.K

def getNp(tau: float, x:float) -> float:
    c1 = 0.036
    c2 = 3.53
    c3 = 0.06696
    #print(tau)
    if tau > 0:
        Np = c1*(math.sqrt(c2*(x**2) + tau)) + c3*x
    else:
        Np = -(c1*(math.sqrt(c2*(x**2) - tau)) + c3*x)
    return Np

def controller(x: float) -> float:
    # sliping variable
    s = x - xd
    # sat function
    sats = max(-1,min(s/phi,1))
    # input as function of x (control)
    u = x*abs(x)*(1.9091*(10**-4) - K*5.18*(10**-5)*sats) - 0.01*sats 
    # thrust
    tau = u*(m - X_added_mass)
    # control allocation
    Np = getNp(tau, x)

    return [s, tau, Np] 