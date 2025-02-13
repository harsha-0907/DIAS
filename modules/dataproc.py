# Functions to help with modifying the datastore

def updateDataStore(alerts):
    from data import dataStore
    # print(type(alerts))
    for alert in alerts:
        city = alert.city
        dataStore[city]["alert_level"] = max(dataStore[city]["alert_level"], alert.alert_level)
        for index, alert_msg in enumerate(dataStore[city]["alerts"]):
            if alert_msg[1] == alert.message:
                # We have updated the already existing alert
                dataStore[city]["alerts"][index][0] = alert.remove_after
                continue
        
        # If the alert is not present then add the alert & update the number of alerts
        dataStore[city]["alerts"].append(alert.message)
        dataStore[city]["numberofalerts"] = len(dataStore[city]["alerts"])
