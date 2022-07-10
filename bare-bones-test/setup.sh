#!/bin/sh

set -x

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate

sudo pip3 install twython

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

Set photo mode with:

  cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt
	
Set tweet mode with:

  cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt

EOF