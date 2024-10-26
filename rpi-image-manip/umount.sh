#!/bin/sh
set -x
sudo sync -f ./boot
sudo umount ./boot
sudo sync -f ./root
sudo umount ./root
rmdir ./boot ./root
