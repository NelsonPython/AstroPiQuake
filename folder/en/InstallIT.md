# Installing software and configuring your device

First, you must configure your Raspberry Pi.  Next, install the SenseHat drivers.  Finally, install the IOTA Python client library, IOTA Python Workshop, and copy the AstroPiOTA scripts.

## Configuring Raspberry Pi

When connecting directly the first time, Raspberry Pi will automatically boot with the default user and password:

```
Default username:  pi
Default password:  raspberry
```

Using the Raspberry Pi Configuration tool, set the keyboard mapping to USA English.  Otherwise, you will be surprised when installation commands fail because the pipe symbol `|` is mapped to `~`.

Click the raspberry icon on the menu, select `Preferences`, then select `Raspberry Pi Configuration`.  Click on the `Localisation` tab.

![RasPi configuration window as described in text](images/Localisation.png)

Set your Locale, Timezone, and WiFi country.  Then, click on the `Set Keyboard...` button.

![Window for setting localisation as described in text](images/localisation2.png)

Select `United States -> English (US)`

## Installing Sense HAT

Install Sense Hat:

```
sudo apt-get update
sudo apt-get install sense-hat
sudo pip-3.2 install pillow
```
See the [driver documentation](https://pythonhosted.org/sense-hat/) for more information

For a quick check, type `python3` at the command line to open an interactive session then tell SenseHat to scroll a "Hello Sense Hat" message across the LED screen:

```
$ python3
>>>from sense_hat import SenseHat
>>>sense = SenseHat()
>>>sense.show_message("Hello Sense Hat")
```

The message, "Hello Sense Hat", will scroll across the Sense Hat LED screen.  Take a look in the <a href="http://www.NelsonGlobalGeek.com/I3/Phase1/AstroPiOTAemulator-HelloSenseHat.htm">AstroPiOTA emulator</a>

To learn more, try all the features of your SenseHat by completing this tutorial:  [Raspberry Pi getting started with Sense Hat](https://projects.raspberrypi.org/en/projects/getting-started-with-the-sense-hat)

## Verifying the version of Python

Verify that Python3 has been pre-installed:

```
python3 --version
$ Python 3.4.2
```

```
pip3 --version
$  pip 18.0 from /usr/local/lib/python3.4/dist-packages/pip-18.0-py3.4.egg/pip (python 3.4)
```

Note:  This tutorial has not been tested using Python 3.6 or 3.7

## Installing the [Python IOTA Workshop scripts](https://github.com/iota-community/python-iota-workshop)

This installs the Pyota client library so you can communicate with the [Tangle](https://docs.iota.org/docs/dev-essentials/0.1/concepts/the-tangle).   The workshop includes a step-by-step tutorial teaching the details of sending and receiving transactions to the Tangle.  They provide the foundation for the code used to store sensor data from AstroPiOTA.

Clone the github repository, install the workshop code, and run the "hello world" example.
```
git clone https://github.com/iota-community/python-iota-workshop.git
cd python-iota-workshop
pip3 install -r requirements.txt
python3 code/e01_hello_world.py
```

The Tangle will respond with the latest statistics:

```
{'appName': 'IRI Testnet',
 'appVersion': '1.8.0-RC1',
 'coordinatorAddress': 'EQQFCZBIHRHWPXKMTOLMYUYPCN9XLMJPYZVFJSAY9FQHCCLWTOLLUGKKMXYFDBOOYFBLBI9WUEILGECYM',
 'duration': 0,
 'features': ['dnsRefresher', 'testnet', 'zeroMessageQueue', 'RemotePOW'],
 'jreAvailableProcessors': 8,
 'jreFreeMemory': 14557498488,
 'jreMaxMemory': 22906667008,
 'jreTotalMemory': 16883646464,
 'jreVersion': '1.8.0_181',
 'lastSnapshottedMilestoneIndex': 434525,
 'latestMilestone': TransactionHash(b'VGIOPUTTHVRKZMSPYLV9RLFGUCXMSZPKXKMQWLJCAZKWGACXUSXMJHCNLHWBVZGLSRTYDUEOAWTTBS999'),
 'latestMilestoneIndex': 1313715,
 'latestSolidSubtangleMilestone': TransactionHash(b'VGIOPUTTHVRKZMSPYLV9RLFGUCXMSZPKXKMQWLJCAZKWGACXUSXMJHCNLHWBVZGLSRTYDUEOAWTTBS999'),
 'latestSolidSubtangleMilestoneIndex': 1313715,
 'milestoneStartIndex': 434527,
 'neighbors': 3,
 'packetsQueueSize': 0,
 'time': 1565638086467,
 'tips': 733,
 'transactionsToRequest': 0}
```

[Running in headless mode](Headless.md)
