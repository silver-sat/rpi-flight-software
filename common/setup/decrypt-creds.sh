#!/bin/sh

set -x
if [ -f $BASE/python/twittercred.py.gpg -a ! -s $BASE/python/twittercred.py ]; then
    if [ "$PASSWORD" = "" ]; then
	stty -echo
        read -p "Encryption password for secret data? " PASSWORD
	stty echo
        grep -v '^export PASSWORD=' /home/pi/.params.sh > /home/pi/.params.sh.tmp
        mv -f /home/pi/.params.sh.tmp /home/pi/.params.sh
        echo "export PASSWORD='$PASSWORD'" >> /home/pi/.params.sh
    fi
    gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d $BASE/python/twittercred.py.gpg > $BASE/python/twittercred.py
fi
