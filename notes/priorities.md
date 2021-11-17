
# Tasks

- Tune controllers
- Find out why pydyna is giving non unique data error for NoWaves p3d file

# Extra

- Make a route for setting different locations in the map
- change name gps_imu_simul to sensors_emul
- change name of simulated state to emulated state

# Report

- remember to rewrite surge control part
- change architectre figure: GUI and colors 
- control allocation subscribes to state also
- fix nomoto equation
- chi_d - beta conflicting convention, since we are using chi_d + beta (sway  convention is different)
- not using gps_imu library anymore, using datasheets
- put eqaution that relates generalized positions and velocities in the report
- change Kalman Filter part a little, we will be using EKF
- update code in appendix
- make a section (in methods) to show the development each block
- yaw controller: intead of tau it's rudder 
- control allocation receives surge velocity from \state topic, not \filtered_state
- The value of LOS paramater R is not clear
- future work: 
  - interpolate between desired velocities (b-splines). Now, there is a relatively large jump in the actuator each time changes waypoint
  - kalman filter

# Code TODOS

- service for getting the updated waypoints (user dragged them in gui) from venus
