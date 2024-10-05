#!/bin/sh

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install -y git 
sudo apt-get install -y ax25-tools 
sudo apt-get install -y ax25-apps 
sudo apt-get install -y gpg 
sudo apt-get install -y raspi-gpio 
sudo apt-get install -y time 
sudo apt-get install -y rfkill 
sudo apt-get install -y python3 
sudo apt-get install -y python3-pip

sudo apt -y autoremove

sudo systemctl stop packagekit
sudo systemctl disable packagekit
