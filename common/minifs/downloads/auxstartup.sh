set -x
. .params.sh
# find rpi-flight-software -type f | fgrep -v '/.git/' | xargs -n 10 md5sum 
# find photos -type f | xargs -n 10 md5sum 
ls -l photos
ifconfig -a
rfkill list
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.1
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.2
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.3
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.4
sh ./.minifs/ul.sh ${GROUND_IP} 5001 .startup.log.5
