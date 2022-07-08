# rpi-flight-software

This repository contains scripts and necessary code to construct specific setups on a raspberry pi for flight, testing, ground-station, etc...

Different subdirectories, to be determined, will hold setups for different contexts, flight, testing, etc. 

Each subdirectory will contain a script, `setup.sh`, that can be run on a clean raspberry pi from the /home/pi directory as the pi user as as follows:

  wget -q -O - 'https://raw.githubusercontent.com/silver-sat/rpi-flight-software/master/<CONFIG>/setup.sh' | sh 
  
where "<CONFIG>" represents the specific setup desired. 

The other contents of the subdirectory have yet to be determined, but these may contain shell scripts or python code to download, execute, or install. The setup script should install any linux packages missing from the raspberry pi instance (using apt-get) and any python modules required (using pi). 

Code and/or scripts that are used in multiple setups shoiuld be put in the common subdirectory.

