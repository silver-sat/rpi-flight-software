#!/bin/sh

set -x

ASPI="runuser -u pi"
cd /home/pi

# Run the camera-test
$ASPI sh /home/pi/.logrotate.sh /home/pi/payload/camera_test.log
$ASPI python3 ./payload/camera_test.py > ./payload/camera_test.log 2>&1

