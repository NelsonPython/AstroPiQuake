## AstroPiQuake

<b>AstroPiQuake gathers environment data using SenseHat and Raspberry Pi</b> 

[AstroPi](https://www.nasa.gov/mission_pages/station/research/experiments/explorer/Investigation.html?#id=7534) flies onboard the International Space Station (ISS) keeping astronauts update-to-date about their environment.  Here on Earth, you can monitor your local environment data and detect earthquakes using a clone of AstroPi called "AstroPiQuake" 

Try out the [AstroPiQuake emulator](https://trinket.io/python/9c2e984979).  Move the temperature slider to see Smiley's face change colors from cool blue to mellow yellow to red hot.  Take a look at [earthquake detection](https://trinket.io/python/86417fad20).  Grab AstroPiQuake with your mouse and shake it.  Watch the graph change as it detects you simulating an earthquake.

### Sensing environment data

Sense Hat has temperature and humidity sensors.  It can sense the barometric pressure.  It has an IMU or Inertial Measurement Unit with an accelerometer that measures acceleration forces, a gyroscope that measures momentum and rotation, and a magnetometer that measures the Earth’s own magnetic field, similar to a compass.  Here are the [technical specifications](SenseHatSpecs.md).

Accelerometer and gyroscope data are measured using [coordinates](https://en.wikipedia.org/wiki/Euler_angles).  These are sometimes referred to as yaw, pitch, and roll.

        x is yaw or rotation about the x-axis
        y is pitch or rotation about the y-axis
        z is roll or rotation about the z-axis
        

## Building your own AstroPiQuake

[Building your own AstroPiQuake environment sensor](BuildIT.md)

[Configuring AstroPiQuake and installing software](InstallIT.md)

[Optional:  running AstroPiQuake in headless mode](Headless.md)

## Getting sensor readings

<a href="viewAstroPiQuake.md">Watching sensor readings</a>

<a href="https://github.com/NelsonPython/DriveI5/blob/master/PublicRadio/AstroPiQuakeTable.md">Saving sensor data in a MySQL table</a>

## Investigating sensor data

[Charting your AstroPiQuake data on ThingSpeak](https://thingspeak.com/channels/865101)

## Experimenting

[Broadcasting messages](https://github.com/NelsonPython/Driving_Experiment).  

Install AstroPiQuake onboard Bumblebee Rover so it can broadcast messages from the rover and other sensors.

[Detecting earthquakes](https://www.kaggle.com/nelsondata/confirming-earthquake-detection).  

Use AstroPiQuake to detect an earthquake.

