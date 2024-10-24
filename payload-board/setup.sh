#!/bin/sh

set -x

. .common/setup/params.sh

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate socat
sudo apt-get remove -y ntp
sudo systemctl stop systemd-timesyncd.service
sudo systemctl disable systemd-timesyncd.service
# sudo systemctl restart dhcpcd.service

setparamifnotset GROUND_IP 192.168.100.101
setparamifnotset GROUND_CALL MYCLL8
setparamifnotset SATELLITE_IP 192.168.100.102
setparamifnotset SATELLITE_CALL MYCLL9
setparamifnotset KISS_MTU 195
setparamifnotset BAUD 9600
setparamifnotset SSDVSIZE 195
setparamifnotset SSDVQUAL 4
setparamifnotset TWITTERCRED edwardsnj.ssapp

# Don't need ax25 if using tncattach
# sudo sed -i "s/MYCALL-0/${SATELLITE_CALL}/" /etc/ax25/axports

# Disable WiFi once setup...
if fgrep -q disable-wifi /boot/config.txt; then
  # Already there, exit peacefully...
  exit 0
fi

sudo sed -e '$r /dev/stdin' -i /boot/config.txt <<EOF
dt-overlay=disable-wifi
EOF

rm -f .minifs
ln -s ".common/minifs" .minifs
rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh
rm -f .gpioreadall.py
ln -s ".common/python/gpioreadall.py" .gpioreadall.py

mkdir -p photos

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

EOF
