#!/bin/sh
touch /home/pi/.runsetup.log
exec >>/home/pi/.runsetup.log 2>&1
set -x

if [ ! -d /home/pi/rpi-flight-software ]; then
  cd /home/pi
  GOOD=0
  for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
    if ping -n -c 1 8.8.8.8 >/dev/null 2>&1; then
      GOOD=1
      break
    fi
    sleep 5
  done
  if [ $GOOD -eq 0 ]; then
    sudo reboot;
  fi
  
  wget --tries=10 --timeout=30 --spider -q -O /dev/null http://google.com/
  if [ $? -ne 0 ]; then
    sudo reboot;
  fi
  
  sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y ntpdate
  if [ $? -ne 0 ]; then
    sudo reboot;
  fi
  
  GOOD=0
  for i in 1 2 3 4 5 6 7 8 9 10 11 12; do
    if sudo ntpdate -u pool.ntp.org; then
      GOOD=1
      break
    fi
    sleep 5
  done
  
  if [ $GOOD -eq 0 ]; then
    sudo reboot;
  fi

  touch /home/pi/.setup.log
  nohup /home/pi/setup.sh XXXXCONFIGXXXX < /dev/null >> /home/pi/.setup.log 2>&1
  if [ -d /home/pi/rpi-flight-software ]; then
    sudo /bin/systemctl disable runsetup.service
    sudo shutdown now
  else
    sudo reboot 
  fi
fi
