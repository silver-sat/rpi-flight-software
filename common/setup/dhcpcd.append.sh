#!/bin/sh

# motify /etc/dhcpcd.conf

set -x

if fgrep -q tnc0 /etc/dhcpcd.conf; then
  # Already there, exit peacefully...
  exit 0
fi

sudo sed -e '$r /dev/stdin' -i /etc/dhcpcd.conf <<EOF

# Suggested by tcnattach documentation
denyinterfaces tnc0
EOF
