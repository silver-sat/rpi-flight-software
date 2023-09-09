#!/bin/sh

set -x

. /home/pi/.params.sh

rfkill unblock wifi

iw dev wlan0 set power_save off

# kissattach -m ${KISS_MTU} -l /dev/serial0 serial 192.168.100.101
# ifconfig ax0 txqueuelen 3
# ifconfig ax0 -arp
# arp -H ax25 -s 192.168.100.102 ${SATELLITE_CALL} 

# sh .logrotate.sh .ax0.log
# axlisten ax0 -a -r -t >/home/pi/.ax0.log 2>&1 &

# use tncattach
sh .logrotate.sh .tnc0.log
/home/pi/.tncattach \
     /dev/serial0 \
	 ${BAUD} \
     -m ${KISS_MTU} \
	 --noipv6 \
     --noup \
     --id ${GROUND_CALL} \
     --interval 600 \
	 -v > .tnc0.log 2>&1 &
sleep 2
ifconfig tnc0 ${GROUND_IP} pointopoint ${SATELLITE_IP}

# iptables -A FORWARD -i ax0 -j ACCEPT
iptables -A FORWARD -i tnc0 -j ACCEPT
iptables --flush -t nat
iptables -t nat -I POSTROUTING -o wlan0 -j MASQUERADE

echo 1 > /proc/sys/net/ipv4/ip_forward

# /etc/init.d/ntp stop
# /etc/init.d/ntp start

sh .logrotate.sh .stunnel.log
stunnel .common/etc/stunnel.conf > .stunnel.log 2>&1 &

sh .logrotate.sh .minifs.log
( cd .minifs; \
  runuser -u pi python3 app.py ${GROUND_IP} > /home/pi/.minifs.log 2>&1 ) &

sh .logrotate.sh .tcpdump.log
tcpdump -i tnc0 -l -A > .tcpdump.log 2>&1 &