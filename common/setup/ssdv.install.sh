#!/bin/sh

set -x

# Apr 14, 2023
COMMIT="bf0249e59db8b9203b9632501bb453b3a653736b"
URL="https://codeload.github.com/fsphil/ssdv/zip/$COMMIT"
cd /home/pi
wget -q -O ssdv.zip "$URL"
unzip ssdv.zip
mv "ssdv-$COMMIT" .ssdvdist
rm -f ssdv.zip
( cd .ssdvdist; make )
ln -s .common/scripts/ssdv.sh .ssdv.sh
ls -l .ssdv
