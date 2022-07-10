#!/bin/sh

set -x

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate

sudo pip3 install twython

rm -f /home/pi/payload
ln -s $BASE /home/pi/payload

rm -f /home/pi/.startup.sh
ln -s /home/pi/payload/startup.sh /home/pi/.startup.sh
chmod a+x /home/pi/.startup.sh
