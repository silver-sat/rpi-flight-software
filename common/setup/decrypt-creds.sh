#!/bin/sh

set -x

#
# To encrypt a new cred file use the following command:
#
#    gpg --no-symkey-cache --passphrase "<password>" --batch -c creds.py
#

. $COMMON/setup/params.sh

for enccredfile in $COMMON/python/*.gpg; do
  credfile=`basename $enccredfile .gpg`
  if [ ! -s "$credfile" ]; then
    getpasswd "Encryption password for secret data? " PASSWORD
    gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d "$enccredfile" > "$credfile"
  fi
done
