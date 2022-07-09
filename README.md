# rpi-flight-software

This repository contains scripts and necessary code to construct specific setups on a raspberry pi for flight, testing, ground-station, etc...

Different subdirectories, to be determined, will hold setups for different contexts, flight, testing, etc. 

Each subdirectory will contain a script, `setup.sh`, that can be run on a clean raspberry pi from the /home/pi directory as the pi user.

Common setup tasks can be found in `common`. A bootstrap script can be used to pull down the repository, carry out common tasks, set some environment variables, and execute the configuration specific setup.sh script. 

```
wget 'https://raw.githubusercontent.com/silver-sat/rpi-flight-software/master/setup.sh'
sh setup.sh <CONFIG>
```

where `<CONFIG>` represents the specific setup desired. setup.sh does not need to be re-downloaded if it is already in place. 


