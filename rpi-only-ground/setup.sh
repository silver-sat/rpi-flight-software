#!/bin/sh

set -x

. .common/setup/params.sh

sudo apt-get install -y ntp stunnel4 socat

echo "restrict 192.168.100.0 mask 255.255.255.0" | \
  sudo sed -e '/#restrict 192.168.123.0/r /dev/stdin' -i /etc/ntp.conf

setparamifnotset SERIAL_PORT 8000
setparamifnotset GROUND_CALL MYCALL-8
setparamifnotset SATELLITE_CALL MYCALL-9
setparamifnotset KISS_MTU 960

sudo sed -i "s/MYCALL-0/${GROUND_CALL}/" /etc/ax25/axports

rm -f .minifs
ln -s ".common/minifs" .minifs
rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

EOF