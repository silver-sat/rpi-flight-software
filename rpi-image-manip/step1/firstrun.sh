#!/bin/sh

touch /boot/firstrun.log
exec >>/boot/firstrun.log 2>&1
set -x

# enable SSH
raspi-config nonint do_ssh 0

# Copy SilverSat startup...
cp -f /boot/setup.sh /home/pi
chown pi.pi /home/pi/setup.sh
chmod +x /home/pi/setup.sh

cp -f /boot/params.sh /home/pi/.params.sh
chown pi.pi /home/pi/.params.sh
rm -f /boot/params.sh

chmod +x /boot/runsetup.sh
cp -f /boot/runsetup.service /etc/systemd/system
chmod -x /etc/systemd/system/runsetup.service
/bin/systemctl enable runsetup.service

# Resize root partition to SD card
raspi-config nonint do_expand_rootfs

shutdown -h now
