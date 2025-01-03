#!/bin/sh

set -x

ASPI="runuser -u pi --"
cd /home/pi

# Turn of HDMI... requires DRM VC4 V3D driver not be enabled...
/usr/bin/tvservice -o

# Guarantee we are in user-space for at least 30 seconds
sleep 30 &
WAITPID=$!

doshutdown() {
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
}

python3 .gpioreadall.py
date
uptime
. /home/pi/.params.sh

# Determine what to do...
MODE=`$ASPI python3 ./payload/mode.py`

if [ "$MODE" = "TWEET" ]; then

  # Set the serial select to RADIO
  $ASPI python3 ./payload/serialselect.py RADIO

  if ! sh ./payload/network-startup.sh ; then
    doshutdown
  fi
  
  time -p $ASPI python3 -u ./payload/tweet.py

  doshutdown

elif [ "$MODE" = "PHOTO" ]; then

  # Set the serial select to CAMERA
  $ASPI python3 ./payload/serialselect.py CAMERA
  
  time -p $ASPI python3 -u ./payload/photo.py
  
  doshutdown

elif [ "$MODE" = "SSDV" ]; then

  $ASPI python3 ./payload/serialselect.py RADIO

  time -p $ASPI python3 -u ./payload/ssdv.py

  doshutdown

else

  true # rfkill unblock wlan

fi
