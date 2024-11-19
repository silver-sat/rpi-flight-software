#!/bin/sh
GROUND_IP=$1
MINIFS_PORT=$2
TARGET=$3
MESSAGE="$4"
PHOTO=$5
set -x
if [ "$PHOTO" != "" -a -f "$PHOTO" ]; then
  curl -F "photo=@${PHOTO}" http://${GROUND_IP}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"\&site=${TARGET}
else
  curl http://${GROUND_IP}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"\&site=${TARGET}
fi
