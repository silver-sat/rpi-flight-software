#!/bin/sh
set -x
if [ "$1" = "" ]; then
  echo "Usage: mount.sh <filesystem>.img" 1>&2
  exit 1
fi
OFFSET=`fdisk -l "$1" | grep W95 | awk '/^[^ ]*1/{ print $2*512 }'`
mkdir boot
sudo mount -o loop,offset=$OFFSET "$1" boot
OFFSET=`fdisk -l "$1" | grep Linux | awk '/^[^ ]*2/{ print $2*512 }'`
mkdir root
sudo mount -o loop,offset=$OFFSET "$1" root
