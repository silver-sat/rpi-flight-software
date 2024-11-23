#!/bin/sh

if [ "$3" = "" ]; then
  echo "Usage: make_filesystem.sh <image> <hostname> <password> [ <release> ]" 1>&2
  exit 1
fi

FS="filesystem-$2.img"

set -x
case "$1" in 
  *.xz) xz -d -c "$1" > "$FS";;
  *.zip) unzip -p "$1" > "$FS";;
  *.img) copy "$1" "$FS";;
  *) exit 1;
esac
qemu-img resize "$FS" 4G

OFFSET=`fdisk -l "$FS" | grep W95 | awk '/^[^ ]*1/{ print $2*512 }'`
BOOT="boot-$2"
mkdir "$BOOT"
sudo mount -o loop,offset=$OFFSET "$FS" "$BOOT"
sudo ./boot-manip.py "$BOOT" step1 "$2" "$3" "$4"
sudo sync -f "./$BOOT"
sudo umount "./$BOOT"
rmdir "./$BOOT"

# docker build -t dockerpi dockerpi
docker run --rm -it -v "./${FS}:/sdcard/filesystem.img" dockerpi 1
docker run --rm -it -v "./${FS}:/sdcard/filesystem.img" dockerpi 2

OFFSET=`fdisk -l "$FS" | grep W95 | awk '/^[^ ]*1/{ print $2*512 }'`
mkdir "$BOOT"
sudo mount -o loop,offset=$OFFSET "$FS" "$BOOT"
sudo ./boot-manip.py "$BOOT" step2 "$2" "$3" "$4"
sudo sync -f "./$BOOT"
sudo umount "./$BOOT"
rmdir "./$BOOT"

rm -f "${FS}.xz"
./pishrink.sh -s -v -n -Z "$FS"
