@echo off
call config.bat
cd %pydyna_pkg_db_path%
ros2 launch pydyna_simple pydyna_simple.launch.py