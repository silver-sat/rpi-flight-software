set -x

# . .params.sh
GROUND_IP=192.168.100.101

###
### Manage shutdown...
###
# ls -l .noshutdown
# touch .noshutdown
rm -f .noshutdown

###
### Check we are at default status by removing 
### override files and explicitly setting all parameters
###
# rm -f .textstatus.txt
# rm -f .photostatus.txt
# rm -f .photo.jpg
# rm -f .noshutdown

# runuser -u pi -- ./setparam.sh TWITTERCRED silversat-ssapp
# runuser -u pi -- ./setparam.sh TWEETTARGET twitter
# runuser -u pi -- ./setparam.sh TWEETMODE proxy
# runuser -u pi -- ./setparam.sh TWEETTEXT IFNOPHOTO

###
### clear the photo folder
###
# rm -f photos/photo-*.jpg
# rm -f photos/thumb-*.jpg
# rm -f photos/ssdv-*.bin
# rm -f photos/last_photo_index.txt

###
### remove all but the last photo taken
###
# rm -f `ls photos/photo-*.jpg | head -n -1`
# rm -f `ls photos/thumb-*.jpg | head -n -1`
# rm -f `ls photos/ssdv-*.bin | head -n -1`

###
### Copy photo to file photo filename - 62265 bytes\
###
# rm -f .photo.jpg
# runuser -u pi -- cp rpi-flight-software/common/etc/overhead.jpg .photo.jpg
# runuser -u pi -- sh ./.minifs/dl.sh ${GROUND_IP} 5001 overhead.jpg .photo.jpg
# runuser -u pi -- scp pi@ground:rpi-flight-software/common/etc/overhead.jpg .photo.jpg

###
### set tweetcreds
###
# runuser -u pi -- ./setparam.sh TWITTERCRED silversat-ssapp
# runuser -u pi -- ./setparam.sh TWITTERCRED edwardsnj-ssapp

# runuser -u pi -- ./setparam.sh BLUESKYCRED silversatorg
# runuser -u pi -- ./setparam.sh BLUESKYCRED edwardsnj

# runuser -u pi -- ./setparam.sh TWEETTARGET twitter
# runuser -u pi -- ./setparam.sh TWEETTARGET bluesky

# runuser -u pi -- ./setparam.sh TWEETMODE direct
# runuser -u pi -- ./setparam.sh TWEETMODE proxy
# runuser -u pi -- ./setparam.sh TWEETMODE minifs

# runuser -u pi -- ./setparam.sh TWEETTEXT IFNOPHOTO
# runuser -u pi -- ./setparam.sh TWEETTEXT ALWAYS

###
### set text tweet...
###
# rm -f /home/pi/.textstatus.txt
# runuser -u pi -- sh ./.minifs/dl.sh ${GROUND_IP} 5001 textstatus.txt /home/pi/.textstatus.txt
# runuser -u pi -- scp pi@ground:downloads/textstatus.txt /home/pi/.textstatus.txt

###
### set photo tweet...
###
# rm -f /home/pi/.photostatus.txt
# runuser -u pi -- sh ./.minifs/dl.sh ${GROUND_IP} 5001 photostatus.txt /home/pi/.photostatus.txt

###
### apply a patch...
###
# PATCH=v1.7.0-v1.7.1.patch
# runuser -u pi -- scp pi@ground:downloads/$PATCH /home/pi/$PATCH
# ( cd rpi-flight-software; runuser -u pi -- patch -f -p1 < /home/pi/$PATCH )
# rm -f /home/pi/$PATCH
#
# Check file...
# grep '^textstatusdefault' rpi-flight-software/common/python/tweet_status.py
# grep '^photostatusdefault' rpi-flight-software/common/python/tweet_status.py

ls -l photos

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
