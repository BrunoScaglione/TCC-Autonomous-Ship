@echo off
call config.bat
IF EXIST %folder% (
    cd %folder%
    del /s /q *.*
)
cd %pydyna_pkg_rosbags_path%
ros2 launch path_following path_following.launch.py