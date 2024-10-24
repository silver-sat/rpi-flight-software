#!/bin/sh

set -x

# everything here should be suitable for running multiple times, 
# on a clean install or after being previously run. It can assume
# an internet connection (usually WiFi).

export GITNAME="rpi-flight-software"

export GITREPO="https://github.com/silver-sat/$GITNAME.git"
export GITURL="https://raw.githubusercontent.com/silver-sat/$GITNAME"
export RFSROOT="/home/pi/$GITNAME"

# Make sure git is installed
sudo DEBIAN_FRONTEND="noninteractive" apt-get update -y
sudo DEBIAN_FRONTEND="noninteractive" apt-get install -y git

# Ensure we are in the pi user's home directory
cd /home/pi

# we execute as the "pi" user, use sudo as needed...
if [ `whoami` != "pi" ]; then
  echo "Execute as user pi"
  exit 1
fi  

# Clone rpi-flight-software repository (this pulls down all configurations)!
if [ ! -d $RFSROOT ]; then
  git clone $GITREPO
  if [ ! -d $RFSROOT ]; then
    echo "git not installed!" 1>&2
	exit 1
  fi
else
  ( cd $RFSROOT; git pull )
fi

# Execute any common setup steps...
export COMMON="$RFSROOT/common"

. $COMMON/setup/params.sh

sh $COMMON/setup.sh

rm -f /home/pi/.common
ln -s $COMMON /home/pi/.common

rm -f .logrotate.sh
ln -s ".common/scripts/logrotate.sh" .logrotate.sh

rm -f setparam.sh
ln -s ".common/scripts/setparam.sh" setparam.sh

rm -f /home/pi/payload
rm -f /home/pi/.startup.sh

# If no specific configuration requested, exit
if [ "$1" = "" -o ! -d "$RFSROOT/$1" ]; then
  set +x
  echo "Available setups...."
	for d in $RFSROOT/*; do
	  if [ -f $d/setup.sh -a $d != "common" ]; then
		  echo "  " `basename $d`
		fi
	done
  exit 0
fi

export BASE="$RFSROOT/$1"

ln -s $BASE /home/pi/payload
ln -s /home/pi/payload/startup.sh /home/pi/.startup.sh

# execute the setup.sh script for the specific configuration
sh payload/setup.sh

