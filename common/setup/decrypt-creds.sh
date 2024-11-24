#!/bin/sh

#
# To encrypt a new cred file use the following command:
#
#    gpg --no-symkey-cache --passphrase "<password>" --batch -c creds.py
#

setopt="$-"
echo "$setopt"
if [ `echo "$setopt" | fgrep x | wc -l` -gt 0 ]; then
  set +x
fi

. $COMMON/setup/params.sh

for enccredfile in $COMMON/*/*.gpg; do
  credfile=`echo "$enccredfile" | sed 's/\.gpg$//'`
  if [ ! -s "$credfile" ]; then
    getpasswd "Encryption password for secret data? " PASSWORD
    gpg --no-symkey-cache --passphrase "$PASSWORD" --batch -d "$enccredfile" > "$credfile"
  fi
done

if [ `echo "$setopt" | fgrep x | wc -l` -gt 0 ]; then
  set -x
fi

# tolerate errors in decryption
exit 0
