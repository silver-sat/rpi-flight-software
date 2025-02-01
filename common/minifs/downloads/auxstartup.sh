set -x

GROUND_IP=192.168.100.101

ls -l photos
ls -l .photo.jpg .textstatus.txt .photostatus.txt

sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
