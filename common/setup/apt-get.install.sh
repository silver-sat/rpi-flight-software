#!/bin/sh

echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

sudo apt update -y
sudo apt upgrade -y
sudo apt dist-upgrade -y
sudo apt autoremove -y

sudo apt install -y git ax25-tools ax25-apps gpg raspi-gpio time rfkill python3 python3-pip

sudo systemctl stop packagekit
sudo systemctl disable packagekit
