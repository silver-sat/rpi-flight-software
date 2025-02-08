set -x

GROUND_IP=192.168.100.101

runuser -u pi -- ./setparam.sh TWEETTARGET bluesky
runuser -u pi -- ./setparam.sh TWEETMODE proxy
runuser -u pi -- ./setparam.sh BLUESKYCRED edwardsnj

cd /home/pi
ls -l photos
for f in .params.sh photos/last_photo_index.txt .textstatus.txt .photostatus.txt .photo.jpg .noshutdown; do
  case $f in 
    *.txt) ;
    *.sh) ;
    .noshutdown) ls -l $f && cat $f ;;
    *.jpg) ls -l $f && md5sum $f ;;
  esac
done
ls -ld .*.log*

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
