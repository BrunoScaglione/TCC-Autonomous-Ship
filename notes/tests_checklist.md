# pydyna_simple

obs: windows uses \ instead of / for dirs

1. build packages in VS terminal as admin
2. run pydyna_simple launch file (already start rosbag)
    1. Open new terminal and source setup.bat of the overlay
    2. run launch file: >> ros2 launch pydyna_simple pydyna_simple.launch.py 
    from C:\Users\bruno\Desktop\tcc-autonomous-ship\src\logs\rosbags
    so that rosbags get created in the same location: pydyna_simple.launch.py
1. inspect topics and service
    1. list topics: >> ros2 topic list -t
    2. rosqt_graph: >> rqt_graph
    3. rosdoctor: >> rosdoctor
2. send topics through cli (inputs)
    1. rudder_angle topic: >> ros2 topic pub /rudder_angle std_msgs/msg/Float32 1
    2. proppeller_rotation topic: >> ros2 topic pub /propeller_rotation std_msgs/msg/Float32 1
3. send request through cli (backend req)
    1. send default req (inital state = 0 and end_simul=False): >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul ""
    2. send with other inital state: >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul "{initial_state: {position: {x: 2, y: 2, psi: 2}, velocity: {u: 3, v: 3, r: 3}}}"
    3. send with end_simul: >> ros2 service call /start_end_simul path_following_interfaces/srv/StartEndSimul "{end_simul: 1}"
4. inspect topic published (state): >> ros2 topic echo state
5. inspect rosbag file (in share/logs)
