#!/bin/sh
#
# Common setup tasks
#
# 1. Ensure various packages are installed
# 2. Setup rc.local hooks
# 3. Add line(s) to axports
#

set -x

sh $BASE/apt-get.install.sh
sh $BASE/rc.local.startup-hook.sh
sh $BASE/axports.append.sh

