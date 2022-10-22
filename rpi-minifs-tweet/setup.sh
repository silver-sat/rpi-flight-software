#!/bin/sh

rm -f .minifs
ln -s ".common/minifs" .minifs

cat <<EOF

Run the minifs webservice in one window:

  python .minifs/app.py
  	
In another window, tweet:

  cd payload
	tweet.py

EOF
