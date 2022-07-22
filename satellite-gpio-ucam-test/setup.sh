#!/bin/sh

set -x

# ntpdate is needed in network-startup.sh
sudo apt-get install -y ntpdate

rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh

cat <<EOF

Run the bootup script manually with:

  sudo runuser -u root sh .startup.sh 

EOF
