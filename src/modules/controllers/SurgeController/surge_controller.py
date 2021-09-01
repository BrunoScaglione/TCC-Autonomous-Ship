import math

import modules.controllers.SurgeController as SurgeController

phi = SurgeController.phi
xd = SurgeController.xd
m = SurgeController.m
X_added_mass = SurgeController.X_added_mass

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
    u = x*abs(x)*(1.9091*(10**-4) + (0.01 + 3.8*(10**-5)*x*abs(x))*sats)
    # thrust
    tau = u*(m - X_added_mass)
    print(f"******* tau = {tau} ************")
    # control allocation
    Np = getNp(u, x)

    return [s, tau, Np] 