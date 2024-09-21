#!/bin/sh

set -x

ASPI="runuser -u pi --"
cd /home/pi

python3 .gpioreadall.py
date
uptime

# Set the SHUTDOWN pins
$ASPI python3 ./payload/shutdown.py RUNNING

# Guarantee we are in user-space for at least 30 seconds
sleep 30 &
WAITPID=$!

# Set the serial select to RADIO
$ASPI python3 ./payload/serialselect.py RADIO

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode.py`

if [ "$MODE" = "TWEET" ]; then
  if ! sh ./payload/network-startup.sh; then
    if [ ! -f .noshutdown ]; then
      wait $WAITPID
      $ASPI python3 ./payload/shutdown.py FINISHED
      python3 .gpioreadall.py
      date
      uptime
      sleep 5
      shutdown -h now
    else
      true # rfkill unblock wlan
    fi
    exit
  fi
fi

if [ "$MODE" = "PHOTO" ]; then
  $ASPI python3 ./payload/serialselect.py CAMERA
  time -p $ASPI python3 -u ./payload/photo.py
  if [ ! -f .noshutdown ]; then
    wait $WAITPID
    $ASPI python3 ./payload/shutdown.py FINISHED
    python3 .gpioreadall.py
    date
    uptime
    sleep 5
    shutdown -h now
  else
    true # rfkill unblock wlan
  fi
elif [ "$MODE" = "TWEET" ]; then
  time -p $ASPI python3 -u ./payload/tweet.py
  if [ ! -f .noshutdown ]; then
    wait $WAITPID
    $ASPI python3 ./payload/shutdown.py FINISHED
    python3 .gpioreadall.py
    date
    uptime
    sleep 5
    shutdown -h now
  else
    true # rfkill unblock wlan
  fi
else
  true # rfkill unblock wlan
fi
