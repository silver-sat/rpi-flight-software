# rpi-only-ground setup

This setup is intended for a raspberry pi representing the ground station attached to the internet by WiFi (usually by the SilverSat SSID) to carry out the basic steps of its mission. This setup also works for a virtual raspberry pi with no hardware connections. 

* It should set up an AX25 over serial via TCP/IP (socat)
* It should bridge its network connect to the AX25 interface
* It should run an NTP daemon for the satellite to set its time with
* It should run the minifs file-server 




