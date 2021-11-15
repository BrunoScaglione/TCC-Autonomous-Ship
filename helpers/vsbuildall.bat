@echo off
call config.bat
call %local_setup_path%
cd %main_ws_path%
rem build specific package with flag "--packages-select path_following"
colcon build --merge-install --symlink-install --event-handlers console_cohesion+