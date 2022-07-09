#!/bin/sh

ASPI="runuser -u pi"
cd /home/pi

# Set the SHUTDOWN pins
$ASPI ./payload/shutdown/main.py

# Determine what to do...
MODE=`$ASPI ./payload/mode/main.py`

if [ "$MODE" = "TWEET" ]; then
  ./payload/network-startup.sh
fi

if [ "$MODE" = "PHOTO" ]; then
  $ASPI ./payload/photo/main.py
  shutdown now
elif [ "$MODE" = "TWEET" ]; then
	$ASPI ./payload/tweet/main.py
	shutdown now
fi
