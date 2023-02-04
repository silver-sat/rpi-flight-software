#!/bin/sh

set -x

. $COMMON/setup/params.sh

if [ -f $COMMON/python/twittercred.py.gpg -a ! -s $COMMON/python/twittercred.py ]; then
  getpasswd "Encryption password for secret data? " PASSWORD
  gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d $COMMON/python/twittercred.py.gpg > $COMMON/python/twittercred.py
fi
if [ -f $COMMON/python/redditcred.py.gpg -a ! -s $COMMON/python/redditcred.py ]; then
  getpasswd "Encryption password for secret data? " PASSWORD
  gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d $COMMON/python/redditcred.py.gpg > $COMMON/python/redditcred.py
fi
