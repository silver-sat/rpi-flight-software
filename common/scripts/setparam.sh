#!/bin/sh

if [ "$1" = "" -o "$2" = "" ]; then
  echo "Usage: setparam.sh PARAMETER value" 1>&2
  exit 1
fi

. /home/pi/.common/setup/params.sh

setparam "$1" "$2"
showparam "$1"