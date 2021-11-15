@echo off
cd /d "%~dp0"
call config.bat
call %underlay_path%
cd %main_ws_path%
rem build specific package with flag "--packages-select path_following"
colcon build --merge-install --symlink-install --event-handlers console_cohesion+