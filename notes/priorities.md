# Remember to account for rudder saturation in yaw control (|delta| < 35 degrees)
# GUI will actually be venus
# Need to make a route for setting different locations in the map
# Make script to delete all logs and bags
# change name gps_imu_simul to sensors_simul

# wave filter is making things worse (introducing bias) instead of helping!
# there doesnt seem to be any wave pertubation (was expecting a 0.25 hz perturbation from the p3d file)!

# speculation:
- zoh block after pydyna and before sensors_simul that publishes all the time (very high publishing rate, aproximating continuos), and put timer in the sensors, so that they read at their rate. Timer will be the period of 
-the sensor rate, the callback you do processing on the data read by the subscriber callback (that is receiving at the publisher rate)
- and the time published by pydyna should have t_step added where t_step is the time
it takes for the computer to run one step of the simulation 

# Report:      
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

# TODOS
- service for getting the updated waypoints from venus server
- desired surge velocity and yaw angle must be set at the beggining by receiving from initial conditions. Will to add some topics or change from service to topic
- angle convention used for rudder angle in venus