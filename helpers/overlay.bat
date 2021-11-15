@echo off

cd /d "%~dp0"
call config.bat
call %overlay_path%
cd %ws_src_path%
