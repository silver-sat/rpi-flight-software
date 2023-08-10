#!/bin/sh

set -x

VERSION="0.1.9"
URL="https://github.com/markqvist/tncattach/releases/download/${VERSION}/tncattach_${VERSION}_armhf.tar.xz"
cd
wget -q -O - "$URL" | xzcat | tar xf -
ln -s tncattach_armhf tncattach
ls -l tncattach/tncattach