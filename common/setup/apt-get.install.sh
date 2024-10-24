#!/bin/sh

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get dist-upgrade -y
sudo apt-get autoremove -y

sudo apt-get install -y git ax25-tools ax25-apps gpg raspi-gpio time rfkill python3 python3-pip

sudo systemctl stop packagekit || true
sudo systemctl disable packagekit || true
