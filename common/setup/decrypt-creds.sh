#!/bin/sh

set -x
if [ -f $BASE/python/twittercred.py.gpg -a ! -s $BASE/python/twittercred.py ]; then
    if [ "$PASSWORD" = "" ]; then
	stty -echo
        read -p "Encryption password for secret data? " PASSWORD
	stty echo
        echo "PASSWORD='$PASSWORD'" >> /home/pi/.params.sh
    fi
    gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d $BASE/python/twittercred.py.gpg > $BASE/python/twittercred.py
fi
