## Initial Image
1. Startup the Raspberry Pi Imager
2. Choose "Raspberry Pi OS (32-bit)"
3. Choose drive "D:\" for SD card
4. Click "Cog" for settings:
   1.  Set image customization options: to always use
   2.  Set hostname to: "satellite" or "ground"
   3.  Enable SSH: use password authentication
   4.  Set username and password: pi, password
   5.  Configure wireless LAN to automatically join: SSID, password
   6.  Set locale to US/New York, keyboard us
   5. Save  
6. Click "WRITE", OK

## Config
1. Open up the config.txt on the SD card filesystem
2. Find the section:
```
# Uncomment some or all of these to enable the optional hardware interfaces
dtparam=i2c_arm=on
#dtparam=i2s=on
dtparam=spi=on
```
and uncomment for spi and i2c.
2. At the end of the file, add
```
enable_uart=1
```
4. Open up the cmdline.txt on the SD card filesystem:
5. Remove `console=serial0,115200` from the beginning of the line

## Initial boot
1. Put the SD card into the RPi and apply power.
2. Wait for it to connect to the network and ssh pi@ipaddress

## Put the setup stuff...
1. At the prompt:
```
wget tinyurl.com/silver-sat-rpi/setup.sh
sh setup.sh <CONFIG>
```
