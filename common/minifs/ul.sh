#!/bin/sh
if [ -f "$3" ]; then
  curl -F "file=@$3" http://${1}:${2}/upload
fi
