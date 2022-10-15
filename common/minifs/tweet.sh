#!/bin/sh
GROUND_IP=$1
MINIFS_PORT=$2
MESSAGE=$3
PHOTO=$4
if [ -f "$4" ]; then
  curl -F "photo=@${PHOTO}" http://${GROUND_ID}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"
  curl http://${GROUND_ID}:${MINIFS_PORT}/tweet?msg="${MESSAGE}"
fi
