
export PARAMS=home/pi/.params.sh

function nothasparam() {
  if [ "${$1}" = "" ]; then
	  true
	else
	  false
	fi
}

function getpasswd() {
  if nothasparam "$1"; then
	  stty -echo
    read -p "$2" "VAR"
	  stty echo
    setparam "$1" "${VAR}"
  fi
}

function getparam() {
  if nothasparam "$1"; then
    read -p "$2[$3]:" "VAR"
    setparam "$1" "${VAR:?$3}"
  fi
}

function setparam() {
  grep "^$1=" /home/pi/.params.sh > /home/pi/.params.sh.tmp
	mv -f /home/pi/.params.sh.tmp /home/pi/.params.sh
  echo "$1='$2'" >> /home/pi/.params.sh
	readparams
}

function setparamifnotset() {
  if nothasparam "$1"; then
    setparam "$1" "$2"
	  readparams
  fi
}

function readparams() {
  if [ -f /home/pi/.params.sh ]; then
    set -a
    . /home/pi/.params.sh
    set +a
  fi
}

export -f nothasparam
export -f readparams
export -f setparam
export -f setparamifnotset
export -f getparam
export -f getpasswd

readparams
