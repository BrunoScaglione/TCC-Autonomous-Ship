@echo off

cd /d "%~dp0"
call config.bat
IF EXIST %path_pkg_logs_path% (
   cd %path_pkg_logs_path%
   del /s /q *.*
)
IF EXIST %path_pkg_rosbags_path% (
   cd %path_pkg_rosbags_path%
   del /s /q *.*
)
ros2 launch path_following path_following.launch.py