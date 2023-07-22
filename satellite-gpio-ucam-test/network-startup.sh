#!/bin/sh

# Network startup stuff...(no ground station, this just sets the time)...

set -x

GOOD=0
for i in 1 2 3 4 5 6 7 8 9 10; do
  if ping -n -c 1 0.debian.pool.ntp.org >/dev/null 2>&1; then
    GOOD=1
    break
  fi
  sleep 5
done

if [ $GOOD -eq 0 ]; then
  exit 1;
fi
ntpdate -u 0.debian.pool.ntp.org || exit 1;
