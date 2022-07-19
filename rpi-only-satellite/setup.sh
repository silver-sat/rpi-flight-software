#!/bin/sh

set -x

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate socat
sudo apt-get remove -y ntp

getparam "Ground IP:" GROUND_IP 

setparamifnotset SERIAL_PORT 8000
setparamifnotset GROUND_CALL MYCALL-8
setparamifnotset SATELLITE_CALL MYCALL-9
setparamifnotset KISS_MTU 960

sudo sed -i "s/MYCALL-0/${SATELLITE_CALL}/" /etc/ax25/axports

rm -f .minifs
ln -s ".common/minifs" .minifs
rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

Set photo mode with:

  cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt
  cp rpi-flight-software/common/etc/overhead.jpg .photo.jpg
	
Set tweet mode with:

  cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt

EOF
