#!/bin/sh

# sudo apt-get update -y
# sudo apt-get dist-upgrade -y

sudo apt-get install -y git ax25-tools ax25-apps gpg

sudo apt -y autoremove

sudo systemctl stop packagekit
sudo systemctl disable packagekit
