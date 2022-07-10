#!/bin/sh

# Network startup stuff...(no ground station, this just sets the time)...

set -x

until ping -n -c 1 0.debian.pool.ntp.org >/dev/null 2>&1; do
  sleep 5
done

ntpdate -u 0.debian.pool.ntp.org
