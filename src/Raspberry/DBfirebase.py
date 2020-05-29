from datetime import datetime
from firebase import firebase
import json

# pip3 install requests
# pip3 install python-firebase

class FBManager:
    def __init__(self):
        self.DB_firebase = firebase.FirebaseApplication("https://heartbeat-c4532.firebaseio.com/", None)
        self.danger = {'danger': False, 'since': datetime.now()}

    def insert(self, jsonDict):
        data = {
            "SensorID": jsonDict["Sensor_ID"],
            "Date_Time": jsonDict["Date"],
            "beats": float(jsonDict["beats"]),
            "beats_level": jsonDict["beatsLevel"],
            "danger": self.manage_danger(jsonDict)
        }
        PersonID = jsonDict["PersonID"]
        self.DB_firebase.post("/heartbeat-c4532/" + PersonID, data)

    def manage_danger(self, json_data):
        date = datetime.strptime(json_data["Date"], '%b %d %Y %I:%M:%S%p')
        interval = date - self.danger["since"]
        if json_data["beatsLevel"] == "Danger":
            if not self.danger["danger"]:
                self.danger["since"] = datetime.now()
                self.danger["danger"] = True
                return False
            elif interval.seconds > 5:  # 60 * 5
                return True
        else:
            if interval.seconds < 3:  # 60 * 3
                self.danger["since"] = datetime.now()
                self.danger["danger"] = False
                return False

# heartbeat-c4532 is the database
# tableName is the tableName
# result = DB_firebase.post("/heartbeat-c4532/00010203-0405-0607-0809-0a0b0c0d0e0f", {"name":"ahmad"})
# result = DBfirebase.get("/heartbeat-c4532/tableName", '')
# result = DBfirebase.put("/heartbeat-c4532/tableName/-M8HIY-cNGsD9lWYjiA2", 'Name', 'Bob')
# result = DBfirebase.delete("/heartbeat-c4532/tableName", '-M8HIY-cNGsD9lWYjiA2')
