# satellite-gpio-ucam-test setup

This setup is intended for a (hardware) raspberry pi representing the satellite payload attached to the internet by WiFi (usually by the SilverSat SSID) to carry out the basic steps of its mission. Hardware elements on the board (GPIO pins, camera) are used. No serial connection for network is required, here, we assume there is a network connection by WiFi.

* It should boot up...
* It should execute a python script to set the Shutdown pins to LOW.
* Execute a python script to determine if it should tweet or take a photo. Since GPIO pins are always HIGH or LOW, one or the other WILL be done. 
* If tweet, it should execute a python script to tweet a photo from its photo directory
* If photo, it should interact with the camera and save a photo to the to the photos directory
* It should shutdown, but currently does not so that tester can login and check the state of the rpi. 

This can be used to test the payload hardware:
1. Set the GPIO pins for photo (all three are LOW)
2. Startup (apply power)
2. Login by ssh, check the .startup.log file etc. check the photos directory
3. Check the (output) shutdown pins (or other wires are LOW). 
4. sudo shutdown now
5. Set the GPIO pins for tweet (all three are HIGH)
6. Startup (apply power)
2. Login by ssh, check the .startup.log file etc. check the photos directory
1. Check the tweet happened. 
5. Rinse, repeat...

Note that the startup script does not shutdown the RPi (at this time). 


