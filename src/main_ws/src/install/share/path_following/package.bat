:: generated from colcon_core/shell/template/package.bat.em
@echo off

:: a batch script is able to determine its own path
:: the prefix is two levels up from the package specific share directory
for %%p in ("%~dp0..\..") do set "COLCON_CURRENT_PREFIX=%%~fp"

call:call_file "%%COLCON_CURRENT_PREFIX%%\share\path_following\hook\cmake_prefix_path.bat"
call:call_file "%%COLCON_CURRENT_PREFIX%%\share\path_following\hook\path_dll.bat"
call:call_file "%%COLCON_CURRENT_PREFIX%%\share\path_following\hook\path.bat"
call:call_file "%%COLCON_CURRENT_PREFIX%%\share\path_following\hook\pythonpath.bat"
call:call_file "%%COLCON_CURRENT_PREFIX%%\share\path_following\hook\ament_prefix_path.bat"

set COLCON_CURRENT_PREFIX=

goto :eof


:: call the specified batch file and output the name when tracing is requested
:: first argument: the batch file
:call_file
  if exist "%~1" (
    if "%COLCON_TRACE%" NEQ "" echo call "%~1"
    call "%~1%"
  ) else (
    echo not found: "%~1" 1>&2
  )
goto:eof
