# rpi-flight-software

This repository contains scripts and necessary code to construct specific setups on a raspberry pi for flight, testing, ground-station, etc...

Different subdirectories, to be determined, will hold setups for different contexts, flight, testing, etc. 

Each subdirectory will contain a script, `setup.sh`, that can be run on a clean raspberry pi from the /home/pi directory as the pi user.

Common setup tasks can be found in `common`. A bootstrap script can be used to pull down the repository, carry out common tasks, set some environment variables, and execute the configuration specific setup.sh script. 

```
wget https://raw.githubusercontent.com/silver-sat/rpi-flight-software/master/setup.sh
sh setup.sh <CONFIG>
```

where `<CONFIG>` represents the specific setup desired. setup.sh does not need to be re-downloaded if it is already in place. 

Note that twitter credentials probably need to be placed in `/home/pi/rpi-flight-software/common/python/twittercred.py`

Once setup, run the .startup script as follows to simulate bootup
```
sudo runuser -u root sh .startup.sh 
```

For the `bare-bones-test` config, which requires no additional hardware other than a network (WiFi) connection, indicate photo mode with:
```
cp rpi-flight-software/common/etc/photo_pins.txt .pins.txt
```
Indicate tweet mode with:
```
cp rpi-flight-software/common/etc/tweet_pins.txt .pins.txt
```

