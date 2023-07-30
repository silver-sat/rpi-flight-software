#!/bin/sh

set -x

ASPI="runuser -u pi"
cd /home/pi

sh ./payload/network-startup.sh
