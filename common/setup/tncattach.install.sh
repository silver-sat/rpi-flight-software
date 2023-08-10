#!/bin/sh

set -x

VERSION="0.1.9"
URL="https://github.com/markqvist/tncattach/releases/download/${VERSION}/tncattach_${VERSION}_armhf.tar.xz"
cd /home/pi
wget -q -O - "$URL" | xzcat | tar xf -
rm -f .tncattach
ln -s tncattach_armhf/tncattach .tncattach
ls -l .tncattach