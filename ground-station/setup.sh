#!/bin/sh

set -x

. .common/setup/params.sh

sudo apt-get install -y ntp stunnel4 socat iptables tcpdump

setparamifnotset GROUND_IP 192.168.100.101
setparamifnotset SATELLITE_IP 192.168.100.102
setparamifnotset KISS_MTU 195
setparamifnotset BAUD 9600
setparamifnotset TWITTERCRED silversat.ssapp
setparamifnotset REDDITCRED silversatorg
setparamifnotset BLUESKYCRED silversatorg
setparamifnotset REDDITSUB silversatorg
delparam GROUND_CALL
delparam SATELLITE_CALL
delparam PASSWORD

if [ `fgrep ${SATELLITE_IP} /etc/ntp.conf | wc -l` -eq 0 ]; then

  echo "restrict ${SATELLITE_IP} mask 255.255.255.255" | \
    sudo sed -e '/#restrict 192.168.123.0/r /dev/stdin' -i /etc/ntp.conf

fi

# don't need if using tncattach
#sudo sed -i "s/MYCALL-0/${GROUND_CALL}/" /etc/ax25/axports

# global setup altered the dhcpcd.conf file...
# sudo systemctl restart dhcpcd.service

rm -f .minifs
ln -s ".common/minifs" .minifs
rm -f uploads
ln -s ".minifs/uploads" uploads
rm -f downloads
ln -s ".minifs/downloads" downloads
rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh

# rm -f .startup.sh

cat <<EOF

Run the folowing command from /home/pi to bridge the payload board

  sudo sh payload/network-startup.sh

EOF
