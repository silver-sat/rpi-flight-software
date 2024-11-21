#!/bin/sh

if [ "$1" = "" ]; then
  echo "Usage: runpi.sh <image>" 1>&2
  exit 1
fi

NAME="rpi"
FS="filesystem-$NAME.img"

set -x
case "$1" in 
  *.xz) xz -d -c "$1" > "$FS";;
  *.zip) unzip -p "$1" > "$FS";;
  *.img) copy "$1" "$FS";;
  *) exit 1;
esac
qemu-img resize "$FS" 6G

# docker build -t dockerpi dockerpi
docker run --rm -it -v "./${FS}:/sdcard/filesystem.img" dockerpi 1
docker run --rm -it -v "./${FS}:/sdcard/filesystem.img" dockerpi 2
