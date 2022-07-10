#!/bin/sh

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate

# Twython python module is required for twitter
sudo pip3 install -y twython

rm -f /home/pi/payload
ln -s $BASE /home/pi/payload

rm -f /home/pi/.startup.sh
ln -s /home/pi/payload/startup.sh /home/pi/.startup.sh
