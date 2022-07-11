#!/bin/sh
#
# Common setup tasks
#
# 1. Ensure various packages are installed
# 2. Setup rc.local hooks
# 3. Add line(s) to axports
#

set -x

if [ -f /home/pi/.params.sh ]; then
  . /home/pi/.params.sh
fi
sh $BASE/setup/apt-get.install.sh
sh $BASE/setup/pip3.install.sh
sh $BASE/setup/rc.local.startup-hook.sh
sh $BASE/setup/axports.append.sh
sh $BASE/setup/decrypt-creds.sh

