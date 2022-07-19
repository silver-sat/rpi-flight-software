
PARAMS=/home/pi/.params.sh

nothasparam() {
  if [ "$(eval echo -n \$$1)" = "" ]; then
	  true
	else
	  false
	fi
}

getpasswd() {
  if nothasparam "$2"; then
	  stty -echo
    read -p "$1" "VAR"
	  stty echo
    setparam "$2" "${VAR}"
  fi
}

getparam() {
  if nothasparam "$2"; then
    read -p "$1[$3]:" "VAR"
    setparam "$2" "${VAR:?$3}"
  fi
}

setparam() {
  grep "^$1=" $PARAMS > $PARAMS.tmp
	mv -f $PARAMS.tmp $PARAMS
  echo "$1='$2'" >> $PARAMS
	readparams
}

setparamifnotset() {
  if nothasparam "$1"; then
    setparam "$1" "$2"
	  readparams
  fi
}

readparams() {
  if [ -f $PARAMS ]; then
    set -a
    . $PARAMS
    set +a
  fi
}

readparams
