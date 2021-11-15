@echo off
cd /d "%~dp0"
call config.bat
cd %pydyna_pkg_db_path%
ros2 launch pydyna_simple pydyna_simple.launch.py