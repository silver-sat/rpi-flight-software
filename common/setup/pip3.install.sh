#!/bin/sh

set -x

sudo python3 -m pip install pyserial==3.5 flask==2.3.3 twython==3.9.1 praw==7.8.1
sudo python3 -m pip install Pillow==8.1.2
python3 -m pip install --user --no-warn-script-location cryptography==41.0.7
python3 -m pip install --user --no-warn-script-location atproto==0.0.55
