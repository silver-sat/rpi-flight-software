#!/bin/sh

if [ "$3" = "" ]; then
  echo "Usage: make_filesystem.sh <image> <hostname> <password>" 1>&2
  exit 1
fi

set -x
case "$1" in 
  *.xz) xz -d -c "$1" > filesystem.img;;
  *.zip) unzip -p "$1" > filesystem.img;;
  *.img) copy "$1" filesystem.img;;
  *) exit 1;
esac
qemu-img resize filesystem.img 4G

OFFSET=`fdisk -l filesystem.img | grep W95 | awk '/^[^ ]*1/{ print $2*512 }'`
mkdir boot
sudo mount -o loop,offset=$OFFSET filesystem.img boot
sudo ./boot-manip.py step1 "$2" "$3"
sudo sync -f ./boot
sudo umount ./boot
rmdir ./boot

docker build -t dockerpi dockerpi
docker run --name dockerpi --rm -it -p 5022:5022 -v ./filesystem.img:/sdcard/filesystem.img dockerpi 1
docker run --name dockerpi --rm -it -p 5022:5022 -v ./filesystem.img:/sdcard/filesystem.img dockerpi 2

OFFSET=`fdisk -l filesystem.img | grep W95 | awk '/^[^ ]*1/{ print $2*512 }'`
mkdir boot
sudo mount -o loop,offset=$OFFSET filesystem.img boot
sudo ./boot-manip.py step2 "$2" ""
sudo sync -f ./boot
sudo umount ./boot
rmdir ./boot

./pishrink.sh -s -v -n -Z filesystem.img
