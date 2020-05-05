## AstroPiQuake

<b>You can sense environment data using SenseHat and Raspberry Pi</b> 

AstroPiQuake is a clone of AstroPi that detects earthquakes.  That's why it's called AstroPiQuake!  [AstroPi](https://www.nasa.gov/mission_pages/station/research/experiments/2429.html) flies onboard the International Space Station (ISS) keeping astronauts update-to-date about their environment.  Here on Earth, you can monitor your local environment data and detect earthquakes. 

Try out the [AstroPiQuake emulator](https://trinket.io/python/9c2e984979).  Move the temperature slider to see Smiley's face change colors from cool blue to mellow yellow to red hot.  Take a look at [earthquake detection](https://trinket.io/python/86417fad20).  Grab AstroPiQuake with your mouse and move it.  Watch the graph change as it detects you simulating an earthquake.

### Sensing environment data

Sense Hat has an IMU or Inertial Measurement Unit with these [specifications](SenseHatSpecs.md):

- Temperature and humidity sensors
- Barometric Pressure sensor
- Accelerometer that measures acceleration forces
- Gyroscope that measures momentum and rotation
- Magnetometer that measures the Earth’s own magnetic field, a bit like a compass

Accelerometer and gyroscope data are measured using [coordinates](https://en.wikipedia.org/wiki/Euler_angles).  These are sometimes referred to as yaw, pitch, and roll.

        x is yaw or rotation about the x-axis
        y is pitch or rotation about the y-axis
        z is roll or rotation about the z-axis
        

## Building your own AstroPiOTA

[Building the environment sensor](BuildIT.md)

[Installing software and configuring your device](InstallIT.md)

[Running in headless mode](Headless.md)


## Investigating your data

[Getting starting with the AstroPiQuake notebook on Kaggle](https://www.kaggle.com/nelsondata/astropiota-weather-los-angeles)

[Charting your data on ThingSpeak](https://thingspeak.com/channels/865101)

## Learning as we go

- As of October 2019, Raspberry Pi Buster operating system appears to have a WiFi Bug.  You may want to use Stretch until a solution is found.  Learn more:  https://www.raspberrypi.org/forums/viewtopic.php?t=252984
