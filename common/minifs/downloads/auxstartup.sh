set -x
find rpi-flight-software -type f | fgrep -v '/.git/' | md5sum 
sh ./.minifs/ul.sh .startup.log .startup.log.1
