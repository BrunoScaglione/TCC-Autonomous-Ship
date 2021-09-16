# pydyna_simple

1. build packages in VS terminal as admin
2. run pydyna_simple launch file (already start rosbag)
    1. Open new terminal and source setup.bat of the overlay
    2. run launch file
    from C:\Users\bruno\Desktop\tcc-autonomous-ship\src\logs\rosbags
    so that rosbags get created in the same location
3. inspect topics and service
    1. rosqt_graph
    2. rosdoctor
4. send topics through cli (inputs)
    1. rudder_angle topic
    2. proppeller_rotation topic
5. send message through cli (backend req)
    1. send default message (inital state = 0 and end_simul=False)
    2. send with other inital state
    3. send with end_simul
6. inspect topic published (state)
7. inspect rosbag file
