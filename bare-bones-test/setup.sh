#!/bin/sh

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate

for f in startup.sh network-startup.sh; do
  rm -f /home/pi/$f
	ln -s $BASE/$f /home/pi/.$f
for d in photo tweet action shutdown; do
  rm -f /home/pi/$d
  ln -s $BASE/$d /home/pi/$d