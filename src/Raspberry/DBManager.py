import sqlite3
import json

DB_Name = "IOT_DB.db"


class DataBaseManager:
    def __init__(self, Person_ID):
        self.conn = sqlite3.connect(DB_Name)
        self.conn.execute("pragma foreign_keys = on")
        self.conn.commit()
        self.Person_ID = Person_ID
        self.cur = self.conn.cursor()

    def add_del_update_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()

    def select_db_record(self, sql_query, args=()):
        self.cur.execute(sql_query, args)
        self.conn.commit()
        return self.cur.fetchall()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    @staticmethod
    def getDataSet(sqlText):
        dbObj = DataBaseManager()
        rows = dbObj.select_db_record()
        del dbObj
        return rows

    def beats_data_handler(self, jsonData):
        jsonDict = json.load(jsonData)
        SensorID = jsonDict["Sensor_ID"]
        PersonID = jsonDict["PersonID"]
        Date_Time = jsonDict["Date"]
        beats = float(jsonDict["beats"])
        beats_level = jsonDict["beats_Level"]
        dbObj = DataBaseManager()
        dbObj.add_del_update_db_record(
            "insert into Heartbeat_data(SensorID, PersonID, Date_Time, beats, beats_Level) values (?,?,?,?,?)",
            [SensorID, PersonID, Date_Time, beats, beats_level])
        del dbObj
        print("Beats successfully in the database\n")

    def sensor_Data_Handler(self, jsonData):
        self.beats_data_handler(jsonData)