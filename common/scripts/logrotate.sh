#!/bin/sh

FILE="$1"
MAXN="${2:-9}"

if [ "$FILE" = "" ]; then
  exit 1
fi

if [ -f "$FILE.$MAXN" ]; then
  rm -f "$FILE.$MAXN"
fi
N1="$MAXN"
N0=`expr $N1 - 1`
while [ $N0 -ge 1 ]; do
  if [ -f "$FILE.$N0" ]; then
	  mv -f "$FILE.$N0" "$FILE.$N1"
	fi
	N1="$N0"
  N0=`expr $N1 - 1`
done
if [ -f "$FILE" ]; then
  mv -f "$FILE" "${FILE}.1"
fi
