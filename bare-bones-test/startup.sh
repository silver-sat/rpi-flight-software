#!/bin/sh

set -x

ASPI="runuser -u pi"
cd /home/pi

# Set the SHUTDOWN pins
$ASPI python3 ./payload/shutdown/main.py

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode/main.py`

if [ "$MODE" = "TWEET" ]; then
  sh ./payload/network-startup.sh
fi

if [ "$MODE" = "PHOTO" ]; then
  $ASPI python3 ./payload/photo/main.py
  echo shutdown now
elif [ "$MODE" = "TWEET" ]; then
  $ASPI python3 ./payload/tweet/main.py
  echo shutdown now
fi
