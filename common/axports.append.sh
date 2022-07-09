
# motify /etc/ax25/axports

if fgrep -q serial /etc/ax25/axports; then
  #Already there, exit peacefully...
	exit 0
fi

sudo sed -e '$r /dev/stdin' -i /etc/ax25/axports <<EOF
serial	MYCALL-0	115200	440	10	Serial interface
EOF
