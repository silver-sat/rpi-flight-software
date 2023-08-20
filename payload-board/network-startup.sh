#!/bin/sh

set -x

. /home/pi/.params.sh

# kissattach to run TCP/IP over serial port
# kissattach -m ${KISS_MTU} -l /dev/serial0 serial 192.168.100.102

# ifconfig ax0 txqueuelen 3
# ifconfig ax0 -arp
# arp -H ax25 -s 192.168.100.101 ${GROUND_CALL}

# sh .logrotate.sh .ax0.log
# axlisten ax0 -a -r -t >/home/pi/.ax0.log 2>&1 &

# use tncattach
sh .logrotate.sh .tnc0.log
/home/pi/.tncattach \
     /dev/serial0 \
	 115200 \
     -m ${KISS_MTU} \
	 --noipv6 \
     --noup \
     --id ${SATELLITE_CALL} \
     --interval 600 \
	 -v > .tnc0.log 2>&1 &
sleep 2
ifconfig tnc0 ${SATELLITE_IP} pointopoint ${GROUND_IP}

GOOD=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  route del default
  sleep 2
  if [ `route | fgrep default | wc -l` -eq 0 ]; then
    GOOD=1
	break
  fi
done
if [ $GOOD -eq 0 ]; then
  exit 1;
fi

GOOD=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  if ping -n -c 1 ${GROUND_IP} >/dev/null 2>&1; then
    GOOD=1
    break
  fi
  sleep 5
done

if [ $GOOD -eq 0 ]; then
  exit 1;
fi

# route add default gw 192.168.100.101 ax0
route add default gw ${GROUND_IP} tnc0

ntpdate -u ${GROUND_IP}

rm -f .auxstartup.sh
sh .minifs/dl.sh ${GROUND_IP} 5001 auxstartup.sh .auxstartup.sh
if [ -f .auxstartup.sh ]; then
  sh .logrotate.sh .auxstartup.log
  sh .auxstartup.sh > .auxstartup.log 2>&1
  sh .minifs/ul.sh ${GROUND_IP} 5001 .auxstartup.log
fi
