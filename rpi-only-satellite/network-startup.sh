#!/bin/sh

set -x

. .params.sh

# Wait until we can ping the GROUND_IP address
until ping -n -c 1 ${GROUND_IP} >/dev/null 2>&1; do
  sleep 5
done

# Create the serial port (over IP)
socat pty,link=/dev/serial0,rawer tcp:${GROUND_IP}:${SERIAL_PORT},retry=11,interval=5  &

# Wait until the serial port is created
until [ -e /dev/serial0 ]; do
  sleep 5
done

# kissattach to run TCP/IP over serial port
kissattach -m ${KISS_MTU} -l /dev/serial0 serial 192.168.100.102
ifconfig ax0 txqueuelen 3
ifconfig ax0 -arp
arp -H ax25 -s 192.168.100.101 ${GROUND_CALL}

sh logrotate.sh .ax0.log
axlisten ax0 -a -r -t >/home/pi/.ax0.log 2>&1 &

route del default || true
route add default gw 192.168.100.101 ax0

ntpdate -u 192.168.100.101

rm -f .auxstartup.sh .auxstartup.log 
.minifs/dl.sh 192.168.100.101 5001 auxstartup.sh .auxstartup.sh
if [ -f .auxstartup.sh ]; then
  sh .logrotate.sh .auxstartup.log
  sh .auxstartup.sh > .auxstartup.log 2>&1
  .minifs/ul.sh 192.168.100.101 5001 .auxstartup.log
fi

