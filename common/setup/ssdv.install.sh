#!/bin/sh

set -x

COMMIT="bf0249e59db8b9203b9632501bb453b3a653736b"
URL="https://codeload.github.com/fsphil/ssdv/zip/$COMMIT"
cd /home/pi
wget -q -O ssdv.zip "$URL"
unzip ssdv.zip
mv "ssdv-$COMMIT" .ssdvdist
rm -f ssdv.zip
( cd .ssdvdist; make )
ln -s .ssdvdist/ssdv .ssdv
ls -l .ssdv
