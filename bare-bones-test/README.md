# bare-bones-test setup

This setup is intended for a raspberry pi, attached to the internet by WiFi (usually by the SilverSat SSID) to carry out the basic steps of its mission. Hardware elements (GPIO pins, camera) are simulated by files in /home/pi.

* It should boot up...
* It should execute a python script to set the Shutdown pins to LOW.
* Execute a python script to determine if it should tweet or take a photo. If none stop without shutting down
* If tweet, it should execute a python script to tweet a photo from its photo directory
* If photo, it should copy a fixed image (later, this should interact with the camera) to the photo directory
* It should shutdown

This can be used to test the RPi software logic:
1. Login by ssh, set the hardware state (photo or tweet)
2. Shutdown
3. Start RPi, it should do as directed, and shutdown
4. Login by ssh, check logs and set hardware state, etc...
5. Rinse, repeat...

Note that the startup script does not shutdown the RPi (at this time). 

The file /home/pi/.pins.txt should indicate the state of pins (BCN numbering)
```
<pin>	HIGH|LOW
```
For photo mode:
```
cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt
```
For tweet mode:
```
cp rpi-flight-software/common/etc/tweet_pins.txt .pins.txt
```



