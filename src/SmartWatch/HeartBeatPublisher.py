import paho.mqtt.client as mqtt
import random, threading, json
from datetime import datetime
from src.SmartWatch.Heartbeat import Heartbeat

Person_UID = "00010203-0405-0607-0809-0a0b0c0d0e0f"
HeartBeatObject = Heartbeat("SENSOR-1", Person_UID)
MQTT_Broker = "test.mosquitto.org"
MQTT_Topic_Heartbeat = "PEOPLE/" + Person_UID + "/HeartBeat"


# rc: return code from the mqtt.
def on_connect(client, userdata, rc):
    if rc != 0:
        print("Unable to connect to the MQTT Broker !!!")
    else:
        print("Connected to the MQTT Broker : " + str(MQTT_Broker))


def on_publish(client, userdata, mid):
    pass


def on_disconnect(client, userdata, rc):
    pass


def publish_to_Topic(Topic, message):
    MQTT_Client.publish(Topic, message)
    print("Published: " + str(message) + " " + " on MQTT Topic " + str(Topic) + "\n")


def getRandomNumber():
    ten = float(10)
    s_rm = 1 - (1 / ten) ** 2
    return (1 - random.uniform(0, s_rm)) ** 0.5


################################################### Methods
def publish_Sensor_Values_to_MQTT():
    threading.Timer(1.0, publish_Sensor_Values_to_MQTT).start()
    beats_value = float("{0:.2f}".format(random.uniform(10, 100) * getRandomNumber()))
    Heartbeats_Data = {}
    Heartbeats_Data['Sensor_ID'] = HeartBeatObject.sensorID
    Heartbeats_Data['PersonID'] = HeartBeatObject.PersonID
    Heartbeats_Data['Date'] = datetime.strftime(datetime.now(), '%b %d %Y %I:%M:%S%p')
    Heartbeats_Data['beats'] = beats_value
    Heartbeats_Data["beatsLevel"] = HeartBeatObject.getBeatsLevel(beats_value)
    Humidity_Json = json.dumps(Heartbeats_Data)
    print("Publishing Beats Value : " + str(beats_value) + " ...")
    publish_to_Topic(MQTT_Topic_Heartbeat, Humidity_Json)


################################################### Vars
MQTT_Client = mqtt.Client("control2")
MQTT_Client.on_connect = on_connect
MQTT_Client.on_disconnect = on_disconnect
MQTT_Client.on_publish = on_publish
MQTT_Client.connect(MQTT_Broker)

publish_Sensor_Values_to_MQTT()
