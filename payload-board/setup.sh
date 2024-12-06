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
setparamifnotset SATELLITE_IP 192.168.100.102
setparamifnotset SATELLITE_CALL WP2XGW
setparamifnotset KISS_MTU 195
setparamifnotset BAUD 9600
setparamifnotset SSDVSIZE 195
setparamifnotset SSDVQUAL 4
setparamifnotset SSDVTIME 300
setparamifnotset SSDVDELAY 1
setparamifnotset TWITTERCRED silversat-ssapp
setparamifnotset REDDITCRED silversat_org
setparamifnotset BLUESKYCRED silversatorg
setparamifnotset REDDITSUB test
setparamifnotset TWEETMODE proxy
setparamifnotset TWEETTARGET twitter
setparamifnotset TWEETTEXT IFNOPHOTO
delparam GROUND_CALL
delparam PASSWORD

showparams

mkdir -p .ssh
cp $COMMON/etc/satellite .ssh/id_ecdsa
cp $COMMON/etc/ground.pub .ssh/authorized_keys
cat $COMMON/etc/satellite.pub >> .ssh/authorized_keys
chmod -R a+rX .ssh
chmod 600 .ssh/id_ecdsa

if [ `fgrep ground /etc/hosts | wc -l` -eq 0 ]; then
  sudo sed -e '/satellite/d' -i /etc/hosts
  echo "${SATELLITE_IP}	satellite" | \
    sudo sed -e '$r /dev/stdin' -i /etc/hosts
  echo "${GROUND_IP}	ground" | \
    sudo sed -e '$r /dev/stdin' -i /etc/hosts
fi

if [ `fgrep "${GROUND_IP}" /etc/resolv.conf | wc -l` -eq 0 ]; then

    # add ground as DNS server...
  echo "nameserver ${GROUND_IP}" | \
    sudo tee /etc/resolv.conf > /dev/null 
  
fi

# Don't need ax25 if using tncattach
# sudo sed -i "s/MYCALL-0/${SATELLITE_CALL}/" /etc/ax25/axports

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
