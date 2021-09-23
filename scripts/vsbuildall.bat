@echo off
call C:\dev\ros2_galactic\install\local_setup.bat
cd "C:\Users\bruno\Desktop\TCC-Autonomous-Ship\src\main_ws"
rem build specific package with flag "--packages-select pydyna_simple"
colcon build --merge-install --symlink-install --event-handlers console_cohesion+ --packages-select path_following