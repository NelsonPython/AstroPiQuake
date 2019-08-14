# Storing sensor data on the Tangle

<b>This code walkthrough explains how to gather environment sensor data from AstroPiOTA and store it in the Tangle</b>

The [getSensorData.py](https://github.com/NelsonPython/AstroPiOTA/blob/master/code/getSensorData.py) script takes one sensor reading and stores data in a log in [csv format](msg-csv.md) and sends data to the Tangle in [dictionary format](msg-dict.md).  For the I3 Data Marketplace demo, it has been scheduled to run one time every 30 minutes.

### Importing libraries


```
#!/usr/bin/python
'''
Purpose: send sensor data to the Tangle

'''
```
In order for sensor data to be meaningful, you must record the date and time the sensor reading was taken so import the time and datetime libraries. 
```
import time
import datetime
```
Data is passed using a json format so import json
```
import json
```
In order for SenseHat to sense data, you must import the SenseHat libraries
```
from sense_hat import SenseHat
```
In order to store data on the Tangle, import Iota client libraries
```
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
```
### sendTX() function
In order to send a transaction to the Tangle, you need two 81-tryte seeds.  The first seed is shown here.  It will send the transaction. Use python-iota-workshop/code/e04_generate_address.py to generate a second seed and attach an address.  Copy that address.  

```
def sendTX(msg):
        seed =    'FIRSTSEED999999999999999999999999999999999999999999999999999999999999999999999999'
        address = 'COPY9NEW9ADDRESS9FROM9SECOND9SEED9HERE9999999999999999999999999999999999999999999'
```
### Setting the testbed

For purposes of testing, connect to the IOTA testbed, called "Devnet"

```
        api = Iota('https://nodes.devnet.iota.org:443',seed)
```
### Sending the data transaction

To send a data transaction, you must format the address, message, tag, and value.  The address is the address that will receive the data.  The message contains the sensor data.  It must be converted to a TryteString.  The tag must be of type "Tag".  The value must be zero.

```
        tx = ProposedTransaction(
                address=Address(address),
                message=TryteString.from_unicode(msg),
                tag=Tag('ASTROPIOTA'),
                value=0
        )
```
There are two steps to sending a transaction:  preparing the transaction and sending the trytes.  In this example, an exception is raised if the transaction cannot be properly prepared.  However, an exception is not raised, if the transaction cannot be sent.

```
        try:
                tx=api.prepare_transfer(transfers=[tx])
        except Exception as e:
                print("Check prepare_transfer ", e)
                raise
        try:
                result=api.send_trytes(tx['trytes'],
                depth=3,min_weight_magnitude=9)
        except:
                print("Check send_trytes")
```
For testing purposes, a copy of data is stored in a CSV file.  Once you are confident in retrieving data from the Tangle, do not store data on the local device because the file becomes too large.

## smiley() function
### Reporting temperature

SenseHat has an 8x8 LED screen.  This function sets the pixels to show a smiley face in different colors depending upon the temperature.

```
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
```
## humidity() function

This function sets the pixels to different colors depending on the humidity levels

```
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
```
## getSensorData() function

This function senses environment data.  It formats the json message that will be sent to the Tangle.  For testing purpose, it saves the data in [csv format](msg-csv.md).  When you are confident in retrieving data from the Tangle, disable this feature because the file will become very large.  

```
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
```
Get the date and time of the sensor reading
```
        t = datetime.datetime.now()
        sensors["timestamp"] = str(t.strftime('%Y%m%d %H:%M'))
        sensors["city"] = 'Los Angeles CA USA'
        sensors["lng"] = '-118.323411'
        sensors["lat"] = '33.893916'
        sensors["device_name"] = "AstroPiOTA"
```
Save the data in csv format
```
        fo = open("/home/pi/I3-Consortium/Data_AstroPiOTA.csv", "a")

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
```
Return data in json format
```
        jsonSensors = json.dumps(sensors)
        return json.loads(jsonSensors), sensors
```
## reportWeather() function

This function changes colors of the LEDs
```
def reportWeather(weatherColor,Q,I,A,sense):
        #black   = (100,100,100)
        #sense.show_message("Pi", text_colour=black, back_colour=weatherColor)
        humidity(Q,I,A, sense)
        time.sleep(3)
        smiley(weatherColor, sense)
        time.sleep(3)

```
## main() function

First, instantiate the SenseHat class and clear the sensors.  Get the sensor data in json and dictionary formats.  The payload is the message that will be sent to the Tangle.  It is formatted using the [dictionary format](msg-dict.md).  Print the sensor data, then send it to the Tangle.
```
def main():
        sense = SenseHat()
        sense.clear()
        jsonSensors, dictSensors = getSensorData(sense)
        payload = ",".join(("{}={}".format(*dictSensor) for dictSensor in dictSensors.items()))
        print(payload)
        sendTX(payload)
```
Set the colors for the LEDs based on the humidity
```

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

```
Set the color of the smiley face to cool blue, mellow yellow, or red hot

![smiley faces described in the text](images/smiley.png)
```
        red     = (150, 0, 0)
        yellow  = (150,100,0)
        blue    = (0,100,150)

        if float(jsonSensors["temperature"]) -5 < 10:
                reportWeather(blue,A,Q,I,sense)
        elif float(jsonSensors["temperature"])-5 < 35:
                reportWeather(yellow,A,Q,I,sense)
        else:
                reportWeather(red,Q,I,A,sense)
```
## Getting started by calling the main function
```
if __name__ == '__main__':
        main()
```
