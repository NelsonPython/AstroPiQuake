#!/usr/bin/python

'''
Purpose: send sensor data to the Tangle

'''
import time
import datetime
import json
from sense_hat import SenseHat
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString

def sendTX(msg):
        seed =    'YOURSEED9999999999999999999999999999999999999999999999999999999999999999999999999'
        address = 'ADDRESS9FROM9DIFFERENT9SEED999999999999999999999999999999999999999999999999999999'
        api = Iota('https://nodes.devnet.iota.org:443',seed)
        tx = ProposedTransaction(
                address=Address(address),
                message=TryteString.from_unicode(msg),
                tag=Tag('ASTROPIOTA'),
                value=0
        )
        try:
                tx=api.prepare_transfer(transfers=[tx])
        except Exceptaion as e:
                print("Check prepare_transfer ", e)
                raise
        try:
                result=api.send_trytes(tx['trytes'],depth=3,min_weight_magnitude=9)
        except:
                print("Check send_trytes")


def smiley(faceColor, sense):
        S = [0,75,70]
        I = faceColor;
        Q = [0,0,70];
        i_pixels = [
                Q,Q,I,I,I,I,Q,Q,
                Q,I,I,I,I,I,I,Q,
                I,I,S,I,I,S,I,I,
                I,I,I,I,I,I,I,I,
                I,I,Q,I,I,Q,I,I,
                I,I,I,Q,Q,I,I,I,
                Q,I,I,I,I,I,I,Q,
                Q,Q,I,I,I,I,Q,Q,
        ];
        sense.set_pixels(i_pixels)

def humidity(A,Q,I,sense):
        S=[100,100,100]
        i_pixels = [
                Q,Q,Q,Q,Q,Q,Q,Q,
                Q,Q,S,Q,Q,S,Q,Q,
                Q,Q,S,Q,Q,S,Q,Q,
                I,I,S,S,S,S,I,I,
                I,I,S,I,I,S,I,I,
                I,I,S,I,I,S,I,I,
                A,A,A,A,A,A,A,A,
                A,A,A,A,A,A,A,A,
        ];
        sense.set_pixels(i_pixels)

def getSensorData(sense):
        sensors = {}
        sensors["pressure"] = str(sense.get_pressure())
        sensors["temperature"] = str(sense.get_temperature())
        sensors["humidity"] = str(sense.get_humidity())

        o = sense.get_orientation()
        sensors["pitch"] = str(o["pitch"])
        sensors["roll"] = str(o["roll"])
        sensors["yaw"] = str(o["yaw"])

        a = sense.get_accelerometer_raw()
        sensors["x"] = str(a["x"])
        sensors["y"] = str(a["y"])
        sensors["z"] = str(a["z"])

        t = datetime.datetime.now()
        sensors["timestamp"] = str(t.strftime('%Y%m%d %H:%M'))
        sensors["city"] = 'Los Angeles CA USA'
        sensors["lng"] = '-118.323411'
        sensors["lat"] = '33.893916'
        sensors["device_name"] = "AstroPiOTA"

        fo = open("/home/pi/I3-Consortium/Data_AstroPiOTA.csv", "a")
        # requires Python 3
        print(sensors["timestamp"],"," \
              ,sensors["lng"],","\
              ,sensors["lat"],","\
              ,sensors["device_name"],","\
              ,sensors["temperature"],","\
              ,sensors["humidity"],","\
              ,sensors["pressure"],","\
              ,sensors["pitch"],","\
              ,sensors["roll"],","\
              ,sensors["yaw"],","\
              ,sensors["x"],","\
              ,sensors["y"],","\
              ,sensors["z"], file=fo)
        fo.close()
        jsonSensors = json.dumps(sensors)
        return json.loads(jsonSensors), sensors

def reportWeather(weatherColor,Q,I,A,sense):
        humidity(Q,I,A, sense)
        time.sleep(3)
        smiley(weatherColor, sense)
        time.sleep(3)

def main():
        sense = SenseHat()
        sense.clear()
        jsonSensors, dictSensors = getSensorData(sense)
        payload = ",".join(("{}={}".format(*dictSensor) for dictSensor in dictSensors.items()))
        sendTX(payload)

        #sense.set_rotation(180)
        if float(jsonSensors["humidity"]) < 20:
                Q = [150,75,0]
                I = [70,0,0]
                A = [150,0,0]
        elif float(jsonSensors["humidity"]) < 70:
                Q = [0,190,0]
                I = [0,100,0]
                A = [0,150,0]
        else:
                Q = [0,75,150]
                I = [0,0,100]
                A = [0,0,150]

        red     = (150, 0, 0)
        yellow  = (150,100,0)
        blue    = (0,100,150)

        if float(jsonSensors["temperature"]) -5 < 10:
                reportWeather(blue,A,Q,I,sense)
        elif float(jsonSensors["temperature"])-5 < 35:
                reportWeather(yellow,A,Q,I,sense)
        else:
                reportWeather(red,Q,I,A,sense)

if __name__ == '__main__':
        main()
