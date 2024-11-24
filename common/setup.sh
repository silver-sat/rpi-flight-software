#!/bin/sh
#
# Common setup tasks
#
# 1. Ensure various packages are installed
# 2. Setup rc.local hooks
# 3. Add line(s) to axports
# 4. Decrypt any files containing secrets
#

set -x

sh $COMMON/setup/apt-get.install.sh || exit 1
sh $COMMON/setup/tncattach.install.sh || exit 1
sh $COMMON/setup/ssdv.install.sh || exit 1
sh $COMMON/setup/pip3.install.sh || exit 1
sh $COMMON/setup/rc.local.startup-hook.sh || exit 1
sh $COMMON/setup/axports.append.sh || exit 1
sh $COMMON/setup/dhcpcd.append.sh || exit 1
sh $COMMON/setup/stop.daily.updates.sh || exit 1
sh $COMMON/setup/decrypt-creds.sh >/dev/null 2>&1 || exit 1
sh $COMMON/setup/git-config.sh || exit 1
echo "Common setup done."
