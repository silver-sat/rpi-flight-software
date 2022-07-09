#!/bin/sh
#
# Common setup tasks
#
# 1. Ensure various packages are installed
# 2. Setup rc.local hooks
# 3. Add line(s) to axports
#

set -x

$BASE/apt-get.install.sh
$BASE/rc.local.startup-hook.sh
$BASE/ax.ports.append.sh