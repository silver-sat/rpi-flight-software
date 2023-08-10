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

sh $COMMON/setup/apt-get.install.sh
sh $COMMON/setup/tncattach.install.sh
sh $COMMON/setup/pip3.install.sh
sh $COMMON/setup/rc.local.startup-hook.sh
sh $COMMON/setup/axports.append.sh
sh $COMMON/setup/decrypt-creds.sh
sh $COMMON/setup/git-config.sh
