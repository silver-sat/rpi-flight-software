set -x
find rpi-flight-software -type f | fgrep -v '/.git/' | md5sum 
sh ./.minifs/ul.sh .startup.log
sh ./.minifs/ul.sh .startup.log.1
