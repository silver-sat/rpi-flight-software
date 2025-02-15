set -x

GROUND_IP=192.168.100.101

cd /home/pi

# Check status of all files that might result changed state of statellite.
ls -l photos
for f in .params.sh photos/last_photo_index.txt .textstatus.txt .photostatus.txt .photo.jpg .noshutdown rpi-flight-software/VERSION; do
  case $f in 
    *.jpg) ls -l $f && md5sum $f ;;
        *) ls -l $f && cat    $f ;;
  esac
done
ls -ld .*.log*

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
