1. To build packages run the following line with the terminal x64 Prompt for Visual Studio 2019, opened as admin,  in the main_ws\src directory:
    1. >> colcon build --merge-install
2. In the command prompt, on the newly created install directory, run:
    1. >> call setup.bat
3. In the same command prompt, now in main_ws\src directory, the node can be started with the line:
    1. >> ros2 launch pydyna_simple pydyna_simple.launch.py
4. In order to verify the topics and services are active, the user may run in a new command prompt, in the same directory:
    1. >> ros2 topic list -t
    2. >> rqt_graph
5. With the pydyna_simple node active, the user can send the topics for rudder_angle and proppeller_rotation, as well as state, but they all must be done in separate command prompts, still in the main_ws\src directory:
    1. rudder_angle topic: 
        1. >> ros2 topic pub --once /rudder_angle std_msgs/msg/Float32 "{data: 0}"
    2. proppeller_rotation topic:
        1. >> ros2 topic pub --once /propeller_rotation std_msgs/msg/Float32 "{data: 1}"
    3. initial state:
        1. >> ros2 topic pub --once /state path_following_interfaces/msg/State "{position: {x: 5, y: 5, psi: 1.571}, velocity: {u: 5, v: 5, r: 5}}"