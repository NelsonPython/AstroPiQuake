#!/usr/bin/python

"""
Purpose: publishing AstroPiOTA environment sensor data
"""

import paho.mqtt.client as mqtt
import time
import datetime
import json
from sense_hat import SenseHat


def on_connect(client, userdata, flags, rc):
    """printing out result code when connecting with the broker

    Args:
        client: publisher
        userdata:
        flags:
        rc: result code

    Returns:

    """

    m="Connected flags"+str(flags)+"\nresult code " +str(rc)+"\nclient1_id  "+str(client)
    print(m)



def on_message(client1, userdata, message):
    """printing out recieved message

    Args:
        client1: publisher
        userdata:
        message: recieved data

    Returns:

    """
    print("message received  "  ,str(message.payload.decode("utf-8")))


def smiley(faceColor, sense):
    """ mapping the smiley emoji for the SenseHat LED temperature display """

    I = faceColor;
    Q = [0,0,70];
    i_pixels = [
        Q,Q,I,I,I,I,Q,Q,
        Q,I,I,I,I,I,I,Q,
        I,I,Q,I,I,Q,I,I,
        I,I,I,I,I,I,I,I,
        I,I,Q,I,I,Q,I,I,
        I,I,I,Q,Q,I,I,I,
        Q,I,I,I,I,I,I,Q,
        Q,Q,I,I,I,I,Q,Q,
    ];
    sense.set_pixels(i_pixels)

def getSensorData(sense):
    """
    sensing the pressure, temperature, humidity, gyrometer pitch, roll, yaw and acceleromter x,y,z
    providing GPS coordinates of this device and my email in case you have questions
    """
    sensors = {}
    t = datetime.datetime.now()
    sensors["timestamp"] = str(t.strftime('%Y%m%d %H:%M'))
    sensors["city"] = 'Los Angeles CA USA'
    sensors["lng"] = '-118.323411'
    sensors["lat"] = '33.893916'
    sensors["device_name"] = "AstroPiOTA"

    sensors["temperature"] = str(sense.get_temperature())
    sensors["humidity"] = str(sense.get_humidity())
    sensors["pressure"] = str(sense.get_pressure())

    o = sense.get_orientation()
    sensors["pitch"] = str(o["pitch"])
    sensors["roll"] = str(o["roll"])
    sensors["yaw"] = str(o["yaw"])

    a = sense.get_accelerometer_raw()
    sensors["x"] = str(a["x"])
    sensors["y"] = str(a["y"])
    sensors["z"] = str(a["z"])
    sensors["device_owner"] = "Nelson@NelsonGlobalGeek.com"

    return sensors

def reportWeather(weatherColor, sense):
    """ reporting the weather on the SenseHat LED screen """

    black   = (100,100,100)
    sense.show_message("Pi", text_colour=black, back_colour=weatherColor)
    smiley(weatherColor, sense)


if __name__ == '__main__':

    # get you account and pw at http://eclipse.usc.edu:8000
    account = 'YOUR-ACCOUNT'
    pw = 'YOUR-PASSWORD'

    # topic is the product you are publishing on the I3 Data Marketplace
    topic = "AstroPiOTA Weather Station"

    try:
        pub_client = mqtt.Client(account)
        pub_client.on_connect = on_connect
        pub_client.on_message = on_message
        pub_client.username_pw_set(account, pw)
        pub_client.connect('18.217.227.236', 1883)      #connect to broker

    except Exception as e:
        print("Exception", str(e))

    sense = SenseHat()
    sense.clear()
    payload = getSensorData(sense)
    print(payload)
    pub_client.publish(topic, json.dumps(payload))
    time.sleep(1)
    pub_client.disconnect()

    # show temperature emoji
    red     = (150, 0, 0)
    yellow  = (150,100,0)
    blue    = (0,100,150)

    # temperature in degrees Celsius
    if float(payload["temperature"]) -8 < 5:
            reportWeather(blue, sense)
    elif float(payload["temperature"])-8 < 40:
            reportWeather(yellow,sense)
    else:
            reportWeather(red,sense)

