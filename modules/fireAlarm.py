# This is the fire alarm module

def fetchSensorMetadata(sesnor_id):
    # Fetch sensor metadata from the db and return city name
    return 'Visakhapatnam'


def updateFireAlerts(sensor_id: int, city: str=None):
    from data import dataStore
    if city is None:
        city = fetchSensorMetadata(sensor_id)  # Fetches sensor data by querying the database, for now disabled
    print(city)
    if city is not None:
        if city not in dataStore:
            from dataproc import newCity
            newCity(city)
        
        now_time = time.time()
        alert = Alert(city = city, alert_level = 3, message = f"A Forest Fire has been detected at {city}. Take necessary precautions",
            disaster="Forest Fire", remove_after=now_time+15)
        
        from dataproc import updateDataStore
        updateDataStore(alert)
        print(f"Updated Fire Alert at - {city}")
    