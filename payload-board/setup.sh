#!/bin/sh

set -x

. .common/setup/params.sh

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate socat
sudo apt-get remove -y ntp
sudo systemctl stop systemd-timesyncd.service
sudo systemctl disable systemd-timesyncd.service

setparamifnotset GROUND_CALL MYCALL-8
setparamifnotset SATELLITE_CALL MYCALL-9
setparamifnotset KISS_MTU 240

sudo sed -i "s/MYCALL-0/${SATELLITE_CALL}/" /etc/ax25/axports

rm -f .minifs
ln -s ".common/minifs" .minifs
rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh
rm -f .gpioreadall.py
ln -s ".common/python/gpioreadall.py" .gpioreadall.py

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

EOF
