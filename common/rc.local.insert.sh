#
# In /home/pi, link the relevant startup script:
#
#   ln -s bridge_startup.sh .startup.sh
#
# or
#
#   ln -s satellite_startup.sh .startup.sh
#
# and
#
#   chmod +x .startup.sh
#
# Logs to /home/pi/.startup.log
#

# Ensure wifi is turned on
rfkill unblock wifi || true

if [ -x /home/pi/.startup.sh ]; then
   /home/pi/.startup.sh >/home/pi/.startup.log 2>&1 &
fi
