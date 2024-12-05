
OLDOPT=$-
# Turn off echo
set +x 

PARAMS=${PARAMS:-/home/pi/.params.sh}

nothasparam() {
  OLDOPT1=$-
  set +x
  if [ "$(eval echo -n \$$1)" = "" ]; then
	  true
  else
	  false
  fi
  set -$OLDOPT1
}

getpasswd() {
  OLDOPT2=$-
  set +x
  if nothasparam "$2"; then
	stty -echo
    read -p "$1" "VAR"
	stty echo
    setparam "$2" "${VAR}"
  fi
  set -$OLDOPT2
}

getparam() {
  OLDOPT3=$-
  set +x
  if nothasparam "$2"; then
    read -p "$1[$3]:" "VAR"
    setparam "$2" "${VAR:?$3}"
  fi
  set -$OLDOPT3
}

setparam() {
  OLDOPT4=$-
  set +x
  grep -v "^$1=" $PARAMS > $PARAMS.tmp
  mv -f $PARAMS.tmp $PARAMS
  echo "$1='$2'" >> $PARAMS
  readparams
  set -$OLDOPT4
}

delparam() {
  OLDOPT5=$-
  set +x
  grep -v "^$1=" $PARAMS > $PARAMS.tmp
  mv -f $PARAMS.tmp $PARAMS
  readparams
  set -$OLDOPT5
}

showparam() {
  OLDOPT6=$-
  set +x
  grep "^$1=" $PARAMS 
  set -$OLDOPT6
}
 
showparams() {
  OLDOPT7=$-
  set +x
  cat $PARAMS 
  set -$OLDOPT7
}
 
setparamifnotset() {
  OLDOPT8=$-
  set +x
  if nothasparam "$1"; then
    setparam "$1" "$2"
    readparams
  fi
  set -$OLDOPT8
}

readparams() {
  OLDOPT9=$-
  set +x 
  if [ -f $PARAMS ]; then
    set -a
    . $PARAMS
    set +a
  fi
  set -$OLDOPT9
}

readparams

set -$OLDOPT
