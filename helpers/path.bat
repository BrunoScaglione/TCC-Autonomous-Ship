@echo off

rem Below code not working, dont know why 
rem call config.bat
rem IF EXIST %folder% (
rem    cd %folder%
rem    del /s /q *.*
rem )
rem cd %pydyna_pkg_rosbags_path%
rem ros2 launch path_following path_following.launch.py

set folder="C:\Users\bruno\Desktop\tcc-autonomous-ship\src\main_ws\install\share\path_following\logs"
IF EXIST %folder% (
    cd %folder%
    del /s /q *.*
)
cd "C:\Users\bruno\Desktop\tcc-autonomous-ship\src\main_ws\install\share\path_following\db\rosbags"
ros2 launch path_following path_following.launch.py