#!/bin/sh

rm -f .minifs
ln -s ".common/minifs" .minifs

cat <<EOF

Run the minifs webservice in one window:

  python3 .minifs/app.py
  	
In another window, tweet:

  cd payload
  export GROUND_IP=127.0.0.1
  python3 tweet.py

EOF
