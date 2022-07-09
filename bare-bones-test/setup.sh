#!/bin/sh

BASEURL="https://raw.githubusercontent.com/silver-sat/rpi-flight-software/master/"

COMMONSCRIPTS="$BASEURL/common/scripts"

# /etc/rc.local startup hook
wget -O - -q "$COMMONSCRIPTS/rc.local.startup-hook.sh" | sh

# linux packages to install
wget -O - -q "$COMMONSCRIPTS/apt-get-install.satellite.sh" | sh

# /etc/axports modification
wget -O - -q "$COMMONSCRIPTS/axports.satellite.append.sh" | sh

SCRIPTS="$BASEURL/satellite/scripts/"

# git-code - reference a specific version? use main branch
https://codeload.github.com/silver-sat/rpi-flight-software/zip/refs/heads/main

