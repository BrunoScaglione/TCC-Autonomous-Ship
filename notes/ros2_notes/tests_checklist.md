# pydyna_simple

obs: windows uses \ instead of / for dirs

1. build packages in VS terminal as admin
2. run pydyna_simple launch file (already start rosbag)
    1. Open new terminal and source setup.bat of the overlay
    2. run launch file: >> ros2 launch pydyna_simple pydyna_simple.launch.py . Launch file is working now! but cant see it process running, using >> ros2 run path_following simul
    3. run launch for other nodes: >> ros2 launch path_following path_following.launch.py
3. inspect topics and servi
    1. list topics: >> ros2 topic list -t
    2. rosqt_graph: >> rqt_graph         
    3. rosdoctor: >> ros2doctor 
4. send topics through cli (inputs)
    1. rudder_angle topic: >> ros2 topic pub --once /rudder_angle std_msgs/msg/Float32 "{data: 0}"
    2. proppeller_rotation topic: >> ros2 topic pub --once /propeller_rotation std_msgs/msg/Float32 "{data: 1}"

    ros2 topic pub --once /propeller_thrust std_msgs/msg/Float32 "{data: 1.0}"  


    1. >> ros2 topic pub --once /waypoints path_following_interfaces/msg/Waypoints "{position: {x: [200.0,400.0,600.0,800.0,1000.0], y: [200.0,400.0,600.0,800.0,1000.0]}, velocity: [1.0,2.0,3.0,4.0,5.0]}"
5. send requ[][]est through cli (backend req)
    1. send default req (inital state = 0 and end_simul=False): >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul "{}"
    2. send with other inital state: >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul "{initial_state: {position: {x: 0, y: 0, psi: 1.571}, velocity: {u: 0, v: 0, r: 0}}}"
    3. send with end_simul: >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul "{end_simul: 1}"
6. inspect topic published (state): >> ros2 topic echo state
7. inspect rosbag file (in share/logs)
