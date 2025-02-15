set -x

GROUND_IP=192.168.100.101

cd /home/pi

# Check we are at default status by explicitly setting all parameters
rm -f .textstatus.txt
rm -f .photostatus.txt
rm -f .photo.jpg
rm -f .noshutdown

runuser -u pi -- ./setparam.sh TWITTERCRED silversat-ssapp
runuser -u pi -- ./setparam.sh TWEETTARGET twitter
runuser -u pi -- ./setparam.sh TWEETMODE proxy
runuser -u pi -- ./setparam.sh TWEETTEXT IFNOPHOTO

# Remove all photos
rm -f photos/photo-*.jpg
rm -f photos/thumb-*.jpg
rm -f photos/ssdv-*.bin
rm -f photos/last_photo_index.txt

# Check status of all files that might result changed state of statellite.
ls -l photos
for f in .params.sh photos/last_photo_index.txt .textstatus.txt .photostatus.txt .photo.jpg .noshutdown; do
  case $f in 
    *.jpg) ls -l $f && md5sum $f ;;
        *) ls -l $f && cat    $f ;;
  esac
done
ls -ld .*.log*

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
