#!/bin/sh

set -x

. .common/setup/params.sh

sudo apt-get install -y ntp stunnel4 socat iptables tcpdump dnsmasq

setparamifnotset GROUND_IP 192.168.100.101
setparamifnotset SATELLITE_IP 192.168.100.102
setparamifnotset KISS_MTU 195
setparamifnotset BAUD 9600
setparamifnotset TWITTERCRED silversat-ssapp
setparamifnotset REDDITCRED silversatorg
setparamifnotset BLUESKYCRED silversatorg
setparamifnotset REDDITSUB silversatorg
delparam GROUND_CALL
delparam SATELLITE_CALL
delparam PASSWORD

showparams

mkdir -p .ssh
cp $COMMON/etc/ground .ssh/id_ecdsa
cp $COMMON/etc/satellite.pub .ssh/authorized_keys
cat $COMMON/etc/ground.pub >> .ssh/authorized_keys
chmod -R a+rX .ssh
chmod 600 .ssh/id_ecdsa

if [ `fgrep satellite /etc/hosts | wc -l` -eq 0 ]; then
  echo "192.168.100.102		satellite\\n192.168.100.101	ground" | \
    sudo sed -e '$r /dev/stdin' -i /etc/hosts
fi

if [ `fgrep ${SATELLITE_IP} /etc/ntp.conf | wc -l` -eq 0 ]; then

  echo "restrict ${SATELLITE_IP} mask 255.255.255.255" | \
    sudo sed -e '/#restrict 192.168.123.0/r /dev/stdin' -i /etc/ntp.conf

fi

if [ `fgrep "server=8.8.8.8" /etc/dnamasq.conf | wc -l` -eq 0 ]; then

  # uncomment these lines...
  sudo sed -e 's/^\#domain-needed/domain-needed/' -i /etc/dnamasq.conf
  sudo sed -e 's/^\#bogus-priv/bogus-priv/' -i /etc/dnamasq.conf
  sudo sed -e 's/^\#no-resolv/no-resolv/' -i /etc/dnamasq.conf
  
  # make these changes...
  sudo sed -e 's/^\#server=.*/server=8.8.8.8\\nserver=8.8.4.4/' -i /etc/dnamasq.conf
  sudo sed -e 's/^\#cache-size=150.*/cache-size=1000/' -i /etc/dnamasq.conf
  sudo sed -e 's/^\#interface.*/interface=tnc0/' -i /etc/dnamasq.conf
  sudo systemctl enable dnsmasq
  
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
