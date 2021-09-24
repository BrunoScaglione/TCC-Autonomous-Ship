@echo off
cd C:\Users\bruno\Desktop\tcc-autonomous-ship\scripts
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/waypoints -d @waypoints.json.txt 
curl -H 'Content-Type: application/json' -X POST http://localhost:5000/inital_condition -d @start.json.txt
curl http://localhost:5000/start  