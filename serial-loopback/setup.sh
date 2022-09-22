#!/bin/sh

set -x

ln -s ./payload/serial_loopback.py 

cat <<EOF

Run the loopback test after login

  python ./serial_loopback.py 

EOF
