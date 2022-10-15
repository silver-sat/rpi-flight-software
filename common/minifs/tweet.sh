#!/bin/sh
GROUND_IP=$1
MINIFS_PORT=$2
MESSAGE=$3
PHOTO=$4
if [ "$PHOTO" != "" -a -f "$PHOTO" ]; then
  curl -F "photo=@${PHOTO}" http://${GROUND_ID}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"
else:
  curl http://${GROUND_ID}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"
fi
