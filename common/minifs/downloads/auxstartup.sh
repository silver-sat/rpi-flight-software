set -x

GROUND_IP=192.168.100.101

cd /home/pi
ls -l photos
for f in .params.sh photos/last_photo_index.txt .textstatus.txt .photostatus.txt .photo.jpg; do
  case $f in 
    *.txt) echo $f && ls -l $f && cat $f ;;
    *.sh)  echo $f && ls -l $f && cat $f ;;
    *.jpg) echo $f && ls -l $f ;;
  esac
done
ls -ld .*.log*

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
