@echo off
cd /d "%~dp0"
call config.bat
cd %payloads_path%
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/waypoints -d @waypoints.json
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/initalCondition -d @start.json
curl http://localhost:5000/start  