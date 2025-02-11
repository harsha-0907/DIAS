#!/bin/python3
# The Progran responsible to run the Server

from fastapi import FastAPI, Response
from helper import readFile
from apscheduler.schedulers.background import BackgroundScheduler
import uvicorn
from model import ClientRequest
from helper import fetchData, updateAlerts, hi, loadPaths

app = FastAPI()

@app.get("/")
def getHomePage():
    return Response(content=readFile("html/hellopage.html"), headers={"Content-Type": "text/html"})

@app.get("/test")
def isWorking():
    return Response(content="{'message': 'Working', 'success': 'true'}", headers={"Content-Type": "application/json"})

@app.post("/getData")
async def fetchData(request: ClientRequest):
    response = None
    if request.api_key is None or request.lat is None or request.lng is None:
        pass
    else:
        if api_key == "ker234kj4kj34j234":
            response = await fetchData(lat, lng)
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
    loadPaths()
    sch = BackgroundScheduler()
    sch.add_job(hi, 'interval', seconds=5)
    sch.start()
    uvicorn.run("server:app", reload=True, host="0.0.0.0", port=8080)