#!/bin/sh

set -x
if [ -f $BASE/python/twittercred.py.gpg -a ! -s $BASE/python/twittercred.py ]; then
  getpasswd "Encryption password for secret data? " PASSWORD
  gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d $BASE/python/twittercred.py.gpg > $BASE/python/twittercred.py
fi
