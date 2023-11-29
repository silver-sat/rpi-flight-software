#!/bin/sh

set -x

ASPI="runuser -u pi --"
cd /home/pi

python3 .gpioreadall.py

# Set the SHUTDOWN pins
$ASPI python3 ./payload/shutdown.py RUNNING

# Set the serial select to RADIO
$ASPI python3 ./payload/serialselect.py RADIO

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode.py`

if [ "$MODE" = "TWEET" ]; then
  if ! sh ./payload/network-startup.sh; then
    $ASPI python3 ./payload/shutdown.py FINISHED
    python3 .gpioreadall.py
    if [ ! -f .noshutdown ]; then
      shutdown -h now
    else
      true # rfkill unblock wlan
    fi
    exit
  fi
fi

if [ "$MODE" = "PHOTO" ]; then
  sleep 120
  $ASPI python3 ./payload/serialselect.py CAMERA
  time -p $ASPI python3 -u ./payload/photo.py
  $ASPI python3 ./payload/shutdown.py FINISHED
  python3 .gpioreadall.py
  if [ ! -f .noshutdown ]; then
    shutdown -h now
  else
    true # rfkill unblock wlan
  fi
elif [ "$MODE" = "TWEET" ]; then
  time -p $ASPI python3 -u ./payload/tweet.py
  $ASPI python3 ./payload/shutdown.py FINISHED
  python3 .gpioreadall.py
  if [ ! -f .noshutdown ]; then
    shutdown -h now
  else
    true # rfkill unblock wlan
  fi
else
  true # rfkill unblock wlan
fi