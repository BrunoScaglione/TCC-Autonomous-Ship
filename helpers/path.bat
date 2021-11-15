@echo off
set folder="C:\Users\bruno\Desktop\tcc-autonomous-ship\src\main_ws\install\share\path_following\logs"
IF EXIST %folder% (
    cd %folder%
    del /s /q *.*
)
cd C:\Users\bruno\Desktop\tcc-autonomous-ship\src\main_ws\install\share\path_following\db\rosbags
ros2 launch path_following path_following.launch.py