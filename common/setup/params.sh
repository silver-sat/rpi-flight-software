
export PARAMS=home/pi/.params.sh

nothasparam() {
  if [ "${$1}" = "" ]; then
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
  grep "^$1=" /home/pi/.params.sh > /home/pi/.params.sh.tmp
	mv -f /home/pi/.params.sh.tmp /home/pi/.params.sh
  echo "$1='$2'" >> /home/pi/.params.sh
	readparams
}

setparamifnotset() {
  if nothasparam "$1"; then
    setparam "$1" "$2"
	  readparams
  fi
}

readparams() {
  if [ -f /home/pi/.params.sh ]; then
    set -a
    . /home/pi/.params.sh
    set +a
  fi
}

export nothasparam
export readparams
export setparam
export setparamifnotset
export getparam
export getpasswd

readparams
