import json
from datetime import datetime
import paho.mqtt.client as mqtt

from src.Raspberry.DBfirebase import FBManager

# MQTT Settings
Person_UID = "00010203-0405-0607-0809-0a0b0c0d0e0f"
MQTT_Broker = "test.mosquitto.org"
MQTT_Topic = "PEOPLE/" + Person_UID + "/HeartBeat"
MQTT_Client = mqtt.Client("control1")

# DATABASES
# DBManager = DataBaseManager(Person_UID)
fbManager = FBManager()


def on_connect(mosq, obj, rc):
    if rc == 0:
        print("connected")
        MQTT_Client.subscribe(MQTT_Topic, 0)  # Subscribe to all Sensors at Base Topic
    else:
        print("bad connection")


def on_message(mosq, obj, msg):
    # print("MQTT Data Received...")
    # print("MQTT Topic: " + msg.topic)
    # print("Data: " + str(msg.payload))
    # DBManager.sensor_Data_Handler(msg.payload)  # Save Data into DB Table
    jsonDict = json.loads(msg.payload)
    fbManager.insert(jsonDict)


def on_subscribe(mosq, obj, mid, granted_qos):
    print("MQTT on_subscribe...")


# initialise
MQTT_Client.on_message = on_message
MQTT_Client.on_connect = on_connect
MQTT_Client.on_subscribe = on_subscribe

# Connect & subscribe
MQTT_Client.connect(MQTT_Broker)
MQTT_Client.subscribe(MQTT_Topic)

MQTT_Client.loop_forever()  # Continue the network loop
