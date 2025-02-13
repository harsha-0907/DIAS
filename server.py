#!/bin/python3
# The Progran responsible to run the Server

from fastapi import FastAPI, Response
from helper import readFile
from apscheduler.schedulers.background import BackgroundScheduler
import uvicorn
from model import ClientRequest
from helper import updateAlerts

app = FastAPI()

@app.get("/")
def getHomePage():
    return Response(content=readFile("html/hellopage.html"), headers={"Content-Type": "text/html"})

@app.get("/test")
def isWorking():
    return Response(content="{'message': 'Working', 'success': 'true'}", headers={"Content-Type": "application/json"})

@app.get("/getData")
async def fetchData(api_key, lat, lng):
    response = None
    request = ClientRequest(api_key=api_key, lat=lat, lng=lng)
    print(request.lat, request.lng, request.api_key)
    if request.api_key is None or request.lat is None or request.lng is None:
        pass
    else:
        if api_key == "ker234kj4kj34j234":
            print("Recieved Request")
            from helper import fetchData
            response_data = fetchData(request.lat, request.lng)
            if response_data is not None:
                import json
                response = Response(content=json.dumps(response_data.json()), headers={"Content-Type": "application/json"})
        else:
            pass
    
    return response

@app.get("/fireAlert")
async def updateFireAlert(sensorId: str = None, city: str = None):
    response = None
    if sensorId is None or city is None:
        # Not Updated
        pass
    else:
        response = await updateFireAlerts(sensorId, city)
    
    return response

if __name__ == "__main__":
    print("Server Running")
    from helper import loadPaths, clearAlerts
    loadPaths()
    from earthquake import updateEarthquakeData
    earth_quake_sch = BackgroundScheduler()
    clear_alerts_sch = BackgroundScheduler()
    earth_quake_sch.add_job(updateEarthquakeData, 'interval', seconds=6)
    clear_alerts_sch.add_job(clearAlerts, 'interval', seconds=5)
    earth_quake_sch.start()
    clear_alerts_sch.start()
    uvicorn.run("server:app", reload=True, host="0.0.0.0", port=8080)