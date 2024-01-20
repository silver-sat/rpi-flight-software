set -x

# . .params.sh
GROUND_IP=192.168.100.101

# sed -i 's/^dtoverlay=vc4-kms-v3d.*/#dtoverlay=vc4-kms-v3d/' /boot/config.txt
# /usr/bin/tvservice -o
# rfkill block wifi

# clear the photo folder
rm -f photos/photo-*.jpg

# 62265 bytes
# cp rpi-flight-software/common/etc/overhead.jpg photo-0000100.jpg

# 41762 bytes
# cp rpi-flight-software/common/etc/group.jpg photo-0000101.jpg

# post to the silversat account
sed -i 's/^TWITTERCRED=.*$/TWITTERCRED="silversat.ssapp"/' /home/pi/.params.sh

# post to the edwardsnj account
# sed -i 's/^TWITTERCRED=.*$/TWITTERCRED="edwardsnj.ssapp"/' /home/pi/.params.sh

echo "/home/pi/.parms.sh"
cat /home/pi/.params.sh

ls -l photos

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
