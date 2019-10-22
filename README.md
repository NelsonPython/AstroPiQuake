## AstroPiOTA

<b>You can sense environment data using SenseHat and Raspberry Pi</b>  You can store the data on the Tangle or sell it on data marketplaces such as [I3 Marketplace](http://ec2-18-217-227-236.us-east-2.compute.amazonaws.com:8000/).

AstroPiOTA is a clone of AstroPi that connects to the IOTA Tangle.  That's why it's called AstroPiOTA!  The Tangle is a distributed ledger useful for storing and sharing data.  

[AstroPi](https://www.nasa.gov/mission_pages/station/research/experiments/2429.html) flies onboard the International Space Station (ISS) keeping astronauts update-to-date about their environment. 
  Here on Earth, you can monitor your local environment data and store it on the Tangle.  

Try out the [AstroPiOTA emulator](http://www.nelsontech.blog/I3/Phase1/AstroPiOTAemulator-Smiley.htm).  Move the temperature slider to see Smiley's face change colors from cool blue to mellow yellow to red hot.  Take a look at [earthquake detection](http://www.nelsontech.blog/I3/Phase1/AstroPiOTAemulator-Earthquake.htm).  Grab AstroPiOTA with your mouse and move it.  Watch the graph change as it detects you simulating an earthquake.

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

## Using your data

You can store your data directly to the Tangle

[Storing data directly to the Tangle](direct2Tangle.md)

[Viewing data using the Devnet Tangle Explorer](https://devnet.thetangle.org/)

[Retrieving data using ZMQ](https://github.com/NelsonPython/IoT-ZMQ-listener/blob/master/README.md)


## Selling your data
You sell data by publishing it on the I3 Marketplace where subscribers can buy it:

[Publishing data to I3 Data Marketplace](I3-publish.md)

[Retrieving your data subscription](I3-subscribe.md)

## Investigating your data

[Getting starting with the AstroPiOTA notebook on Kaggle](https://www.kaggle.com/nelsondata/astropiota-weather-los-angeles)

[Charting your data on ThingSpeak](https://thingspeak.com/channels/865101)

## Learning as we go

- Seeds are only needed for sending value transactions

- Raspberry Pi Buster operating system appears to have a WiFi Bug.  You may want to use Stretch until a solution is found.  Learn more:
https://www.raspberrypi.org/forums/viewtopic.php?t=252984

- Python 3.7.3 is not fully supported by PYOTA.  See [CO2-TVOC](https://github.com/NelsonPython/CO2TVOC) for a work around

