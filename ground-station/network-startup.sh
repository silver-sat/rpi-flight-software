#!/bin/sh

set -x

. /home/pi/.params.sh

kissattach -m ${KISS_MTU} -l /dev/serial0 serial 192.168.100.101
ifconfig ax0 txqueuelen 3
ifconfig ax0 -arp
arp -H ax25 -s 192.168.100.102 ${SATELLITE_CALL} 

sh .logrotate.sh .ax0.log
axlisten ax0 -a -r -t >/home/pi/.ax0.log 2>&1 &

iptables -A FORWARD -i ax0 -j ACCEPT
iptables --flush -t nat
iptables -t nat -I POSTROUTING -o eth0 -j MASQUERADE

echo 1 > /proc/sys/net/ipv4/ip_forward

/etc/init.d/ntp stop
/etc/init.d/ntp start

sh .logrotate.sh .stunnel.log
stunnel .common/etc/stunnel.conf > .stunnel.log 2>&1 &

( cd .minifs; \
  sh /home/pi/.logrotate.sh app.log; \
	runuser -u pi python app.py > app.log 2>&1 ) &