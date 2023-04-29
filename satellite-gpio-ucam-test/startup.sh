#!/bin/sh

set -x

ASPI="runuser -u pi -- "
cd /home/pi

gpio readall

# Set the SHUTDOWN pins
$ASPI python3 ./payload/shutdown.py RUNNING

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode.py`

if [ "$MODE" = "TWEET" ]; then
  sh ./payload/network-startup.sh
fi

if [ "$MODE" = "PHOTO" ]; then
  sleep 120
  time -p $ASPI python3 -u ./payload/photo.py
  $ASPI python3 ./payload/shutdown.py FINISHED
  gpio readall
  shutdown -h now
elif [ "$MODE" = "TWEET" ]; then
  time -p $ASPI python3 -u ./payload/tweet.py
  $ASPI python3 ./payload/shutdown.py FINISHED
  gpio readall
  shutdown -h now
fi
