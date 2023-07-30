# rpi-only-satellite setup

This setup is intended for a raspberry pi representing the satellite payload to carry out its mission using a ground station raspberry pi to connect to the internet. See the rpi-only-ground for the ground rpi setup. Virtual rpis communicate using AX.25 over socat, which simulates a serial connection over TCP/IP. Hardware elements (GPIO pins, camera, serial connection) are simulated by files in /home/pi or software daemons. This is a more complete infrastructure than bare-bones-test because it includes:

* setting the satellite payload rpi clock from the ground station rpi
* pulling additional startup script from the ground and returning logs to the ground
* AX.25 setup for serial connection based internet and network bridging on the ground station rpi
* Twitter proxy (http -> https) to ensure connections are not encrypted.

Much of this functionality was originally implemented in the silver-sat/arduinotnc repository.

Some of this functionality requires considerable support from the ground station rpi. See the [bare-bones-test setup](../bare-bones-test/#readme) for information about how to "control" the file-based payload settings. 

The IP address of the ground station rpi is required. The setup script will query the user for this IP address if it is not already present in the `/home/pi/.params.sh` file.
```
GROUNDIP=<IP address of ground station RPi>
```




