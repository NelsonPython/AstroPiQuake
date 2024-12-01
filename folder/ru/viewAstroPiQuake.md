<h1>Viewing AstroPiQuake sensor data</h1>

<b>AstroPiQuake senses temperature, humidity, and pressure.  It gets gyroscope and accelerometer readings.</b>

This getData.py script senses data and prints it in json format

```
#!/usr/bin/python

import datetime
from sense_hat import SenseHat

sense = SenseHat()

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
sensors["lng"] = '-118.323411'
sensors["lat"] = '33.893916'
sensors["device_name"] = "AstroPiQuake"

print(sensors)
```

<h3>json</h3>

```
{'pressure': '0', 'lat': '33.893916', 'z': '-0.02169257216155529', 'pitch': '2.6417886780271713', 'roll': '281.7232590548508', 'yaw': '134.7106325472459', 'lng': '-118.323411', 'y': '-0.972381591796875', 'humidity': '39.247840881347656', 'device_name': 'AstroPiQuake', 'x': '-0.0034556991886347532', 'timestamp': '20200528 12:31', 'temperature': '31.669998168945312'}
```
