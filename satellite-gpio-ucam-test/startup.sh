#!/bin/sh

set -x

ASPI="runuser -u pi"
cd /home/pi

# Set the SHUTDOWN pins
$ASPI python3 ./payload/shutdown.py

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode.py`

if [ "$MODE" = "TWEET" ]; then
  sh ./payload/network-startup.sh
fi

if [ "$MODE" = "PHOTO" ]; then
  sleep 120
  $ASPI python3 ./payload/photo.py
  echo shutdown now
elif [ "$MODE" = "TWEET" ]; then
  $ASPI python3 ./payload/tweet.py
  echo shutdown now
fi
