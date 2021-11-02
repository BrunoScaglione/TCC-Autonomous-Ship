import math

import modules.controllers.SurgeController as SurgeController

Kp = SurgeController.Kp
Kd = SurgeController.Kd
Ki = SurgeController.Ki
psid = SurgeController.psid

def controller(counter, r, psi: float) -> float:
    
    psi_barra = psi - psid
    
    tau = Kp * psi_barra + Kd * r + Ki * counter
    
    if tau > 0.6108:
        tau = 0.6108
        
    if tau < -0.6108:
        tau = -0.6108
    
    counter = counter + psi_barra
    
    if counter > 0.5:
        counter = 0.5
        
    if counter < -0.5:
        counter = -0.5
    
    return tau, counter

