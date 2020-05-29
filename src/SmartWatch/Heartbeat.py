
class Heartbeat(object):
    def __init__(self, sensorID, Person_ID):
        self.sensorID = sensorID
        self.PersonID = Person_ID
        print("new instance of this model")

    def getBeatsLevel(self, beats):
        if beats <= 30:
            return "Better"
        elif beats >= 40 and beats <= 90:
            return "Normal"
        else:
            return "Danger"

