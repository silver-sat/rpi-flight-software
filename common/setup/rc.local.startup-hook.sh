#!/bin/sh

# modify /etc/rc.local
set -x

if fgrep -q .startup.sh /etc/rc.local; then
  # Already there, exit peacefully...
  exit 0
fi

sudo sed -e '$r /dev/stdin' -e '/exit 0/d' -i /etc/rc.local <<EOF
#
# In /home/pi, link or copy the startup script to /home/pi/.startup.sh
#
# Logs to /home/pi/.startup.log
#

# Ensure wifi is turned on
rfkill unblock wifi || true

if [ -x /home/pi/.startup.sh ]; then
   if [ -f /home/pi/.startup.log ]; then
	    # put logrotate in here?
	    mv -f /home/pi/.startup.log /home/pi/.startup.log.old
	 fi
   /home/pi/.startup.sh > /home/pi/.startup.log 2>&1 &
fi
exit 0
EOF
chmod a+x /etc/rc.local
