#!/bin/sh

ASPI="runuser -u pi"
cd /home/pi

# Set the SHUTDOWN pins
$ASPI ./shutdown/main.py

# Determine what to do...
MODE=`$ASPI ./mode/main.py`

if [ "$MODE" = "TWEET" ]; then
  ./.network-startup.sh
fi

if [ "$MODE" = "PHOTO" ]; then
  $ASPI ./photo/main.py
  shutdown now
elif [ "$MODE" = "TWEET" ]; then
	$ASPI ./tweet/main.py
	shutdown now
fi
