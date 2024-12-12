set -x

# . .params.sh
GROUND_IP=192.168.100.101

rm -f .noshutdown

# clear the photo folder
# rm -f photos/photo-*.jpg
# rm -f photos/thumb-*.jpg
# rm -f photos/ssdv-*.bin

# Copy photo to file photo filename - 62265 bytes
runuser -u pi -- cp rpi-flight-software/common/etc/overhead.jpg .photo.jpg

# set tweetcreds
runuser -u pi -- setparam.sh TWITTERCRED edwardsnj-ssapp

# set text tweet...
rm -f /home/pi/.textstatus.txt
runuser -u pi -- sh ./.minifs/dl.sh ${GROUND_IP} 5001 textstatus.txt /home/pi/.textstatus.txt

# set photo tweet...
rm -f /home/pi/.photostatus.txt
runuser -u pi -- sh ./.minifs/dl.sh ${GROUND_IP} 5001 photostatus.txt /home/pi/.photostatus.txt

ls -l photos

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
