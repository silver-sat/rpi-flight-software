#!/bin/sh

# motify /etc/dhcpcd.conf

set -x

if fgrep -q tnc0 /etc/etc/dhcpcd.conf; then
  # Already there, exit peacefully...
  exit 0
fi

sudo sed -e '$r /dev/stdin' -i /etc/dhcpcd.conf <<EOF
denyinterfaces ax0
denyinterfaces tnc0
EOF
