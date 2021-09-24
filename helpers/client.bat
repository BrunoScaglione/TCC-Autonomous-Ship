@echo off
cd C:\Users\bruno\Desktop\tcc-autonomous-ship\scripts
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/waypoints -d @waypoints.json
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/inital_condition -d @start.json
curl http://localhost:5000/start  