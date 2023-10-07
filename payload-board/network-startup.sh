#!/bin/sh

set -x

. /home/pi/.params.sh

# kissattach to run TCP/IP over serial port
# kissattach -m ${KISS_MTU} -l /dev/serial0 serial ${SATELLITE_IP}

# ifconfig ax0 txqueuelen 3
# ifconfig ax0 -arp
# arp -H ax25 -s ${GROUND_IP} ${GROUND_CALL}

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
  --id ${SATELLITE_CALL} \
  --interval 600 \
	-v > .tnc0.log 2>&1 &
sleep 2
ifconfig tnc0 ${SATELLITE_IP} pointopoint ${GROUND_IP}

GOOD=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  if ping -I tnc0 -n -c 1 ${GROUND_IP} >/dev/null 2>&1; then
    GOOD=1
    break
  fi
  sleep 5
done

if [ $GOOD -eq 0 ]; then
  exit 1;
fi

# route add default gw ${GROUND_IP} ax0
route add default gw ${GROUND_IP} tnc0

GOOD=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  if ntpdate -u ${GROUND_IP}; then
    GOOD=1
    break
  fi
  sleep 5
done

if [ $GOOD -eq 0 ]; then
  exit 1;
fi

if [ "${TWITTERCRED}" != "" ]; then
  rm -f rpi-flight-software/common/python/twittercred.py 
  ln -s rpi-flight-software/common/python/twittercred.${TWITTERCRED}.py \
        rpi-flight-software/common/python/twittercred.py 
fi

rm -f .auxstartup.sh
sh .minifs/dl.sh ${GROUND_IP} 5001 auxstartup.sh .auxstartup.sh
if [ -s .auxstartup.sh ]; then
  sh .logrotate.sh .auxstartup.log
  sh .auxstartup.sh > .auxstartup.log 2>&1
  sh .minifs/ul.sh ${GROUND_IP} 5001 .auxstartup.log
fi
