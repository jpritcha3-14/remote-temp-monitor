# remote-temp-monitor
Remote temperature monitor on RPi targeting AWS to send SNS alerts

The goal of this project was to create a small IoT device to monitor the temperature of my friend's apartment and make sure it's not getting too hot for his dog while he's away.

The project uses a [18B20 1-wire temperature sensor](http://www.circuitbasics.com/raspberry-pi-ds18b20-temperature-sensor-tutorial/) sitting on a headless Raspberry Pi Zero W to get the ambient temperature.  The temperature is continuously monitored by [publish_temp.py](https://github.com/jpritcha3-14/remote-temp-monitor/blob/master/publish_temp.py) and if the set threshold is exceeded, it is published to an AWS topic.  An AWS Lambda function subscribes to the topic and relays any messages it recieves to AWS SNS which sends text alerts to my friend's phone.

start.sh is registered as a service with systemd to both run on startup and recover automatically if publish_temp.py fails.  This makes the device mostly a plug and play/set and forget interface.

### Future Improvements
* Add a mobile front end (React Native with AWS Amplify?) for temperature monitoring
* Allow user to change temperature threshold and alert backoff time (small db for persistent parameter storage)
* Have AWS monitor the status of the device and send an alert if there is extended downtime.
