#!/bin/sh

. /home/pi/.params.sh

IMGFN="$1"
SSDVFN="$2"

if [ "$IMGFN" = "" ]; then
  exit 1
fi

if [ "$SSDVFN" = "" ]; then
  exit 1
fi

INDEX=`echo "$IMGFN" | sed -n 's/^.*thumb-\([0-9]*\)\.jpg$/\1/p'`
INDEX=`expr $INDEX % 256`

SSDV=/home/pi/.ssdvdist/ssdv
echo ssdv -e -n -c \""$SATELLITE_CALL"\" -i \""$INDEX"\" -q \""$SSDVQUAL"\" -l \""$SSDVSIZE"\" \""$IMGFN"\" \""$SSDVFN"\"
$SSDV -e -n -c "$SATELLITE_CALL" -i "$INDEX" -q "$SSDVQUAL" -l "$SSDVSIZE" "$IMGFN" "$SSDVFN"
