#!/bin/sh

# Network startup stuff...(no ground station, this just sets the time)...

set -x

ntpdate -u 0.debian.pool.ntp.org
