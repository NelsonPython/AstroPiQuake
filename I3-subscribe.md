# Subscribing to I3 Data Marketplace data

<b>This code walkthrough explains how to subscribe to AstroPiOTA data published at the I3 Data Marketplace.</b>  AstroPiOTA publishes environment data every 30 minutes.

## Setting up your subscription
Follow the [Connecting an IoT Device to the I3 Data Marketplace](https://github.com/NelsonPython/Connect_IoT_Device_to_I3) guide and subscribe to AstroPiOTA

## Subscribing to data
```
#!/usr/bin/python

"""
Purpose:  subscribing to AstroPiOTA data from I3 Consortium Data Marketplace at http://eclipse.usc.edu:8000
"""
```

Import the [Eclipse Paho MQTT Python client library](https://pypi.org/project/paho-mqtt/) so you can subscribe to your data
```
import paho.mqtt.client as mqtt
```
In order for your data to be meaningful, you must report the time it was sensed.  Import time and datetime libraries

```
import time
import datetime
```
Data is passed using a json format so import json libraries
```
import json
```
Import the Iota libraries so you can send a transaction to the Tangle
```
from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
```
### on_connect function

This function connects to the broker and prints the status of the connection
```
def on_connect(client, userdata, flags, rc):
    """ reporting IoT device connection """

    try:
        m = "Connected flags " + str(flags) + "\nResult code " + str(rc) + "\nClient_id  " + str(client)
        print(m)
        print("\n")
    except e:
        print("Hmmm I couldn't report the IoT connection: ", e)
```
### on_message function

This function receives data, prints it, stores it in csv format in the AstroPiOTA.csv file, and stores it on the IOTA Tangle

```
def on_message(client, userdata, msg):
    """ receiving data"""

    try:
        sensors = msg.payload
        sensors = json.loads(sensors.decode('utf-8'))
    except e:
        print("Check the message: ",e)

    logfile = open("AstroPiOTA.csv","a")
    print(str(sensors["timestamp"]),",",str(sensors["lng"]),",",\
        str(sensors["lat"]),",",str(sensors["device_name"]),",",str(sensors["temperature"]),",",\
        str(sensors["humidity"]),",",str(sensors["pressure"]),",",str(sensors["pitch"]),",",\
        str(sensors["roll"]),",",str(sensors["yaw"]),",",str(sensors["x"]),",",\
        str(sensors["y"]),",",str(sensors["z"]),",",str(sensors["device_owner"]),",",str(sensors["city"]),file=logfile)
    logfile.close()
```
Print the data to the screen
```
    # this prints the AstroPiOTA data message
    print("\nTimestamp: ", str(sensors["timestamp"]))
    print("Device: ", sensors["device_name"])
    print("Device owner email: ", sensors["device_owner"])
    print("Device location: ", sensors["city"], " at longitude: ", sensors["lng"], " and latitude: ", sensors["lat"])

    print("Temperature: ", sensors["temperature"])
    print("Humidity: ", sensors["humidity"])
    print("Pressure: ", sensors["pressure"])

    print("Pitch: ", sensors["pitch"])
    print("Roll: ", sensors["roll"])
    print("Yaw: ", sensors["yaw"])

    print("Accelerometer x: ", sensors["x"])
    print("Accelerometer y: ", sensors["y"])
    print("Accelerometer z: ", sensors["z"])
```
Store the data in the Tangle
```
    api = Iota('https://nodes.devnet.iota.org:443') 
    address = '999999999999999999999999999999999999999999999999999999999999999999999999999999999'
    tx = ProposedTransaction(
        address=Address(address),
        #message=TryteString.from_unicode(sensors),
        message=TryteString.from_unicode(json.dumps(sensors)),
        tag=Tag('ASTROPIOTAIIIDEMO'),
        value=0
    )
    try:
        tx = api.prepare_transfer(transfers=[tx])
    except:
        print("PREPARE EXCEPTION",tx)
    try:
        result = api.send_trytes(tx['trytes'], depth=3, min_weight_magnitude=9)
    except:
        print("EXCEPTION", result)
```
### test_sub() function
This is the main loop.  The broker address and port are provided.

```
def test_sub():
    '''
    Broker address: 18.217.227.236 
    (ec2-18-217-227-236.us-east-2.compute.amazonaws.com)
    Broker port: 1883
    '''
```
Enter the topic you subscribed to along with your account and password
```    
    topic = "AstroPiOTA"
    account = 'YourAccount'
    pw = 'YourPassword'
```
Connect to the broker
```
    sub_client = mqtt.Client(account)
    sub_client.on_connect = on_connect
    sub_client.on_message = on_message
    sub_client.username_pw_set(account, pw)
    sub_client.connect('18.217.227.236', 1883, 60) #connect to broker
    sub_client.subscribe(topic)
```
This script will listen until it is interrupted.  
```
    rc = sub_client.loop_forever()
    time.sleep(1)
    print("Return code ", rc)
```
Test_sub is a loop.  It can be stopped using the keyboard interrupt, ```ctrl-c```.
```
if __name__ == '__main__':
    try:
        test_sub()
    except KeyboardInterrupt:
        rc = sub_client.loop_stop()
        print("\nI'm stopping now")
```
### Sample output

<img src="images\Screenshot from 2019-08-13 19-58-21.png")
