
import sys, time

import find_common_modules

from gpio_pins import init_pins, read_pins, write_pins
from pins import STATES, SHUTDOWN
from vote import voting

HIGH = True
LOW = False

# See shutdown.py for logic

# initialize pins
init_pins(inpins=STATES,outpins=SHUTDOWN)

# read STATES pins
pins1 = read_pins(STATES,1)

if None in pins1:
    sys.exit(0)
    
time.sleep(2)

write_pins(SHUTDOWN, LOW) # False/LOW indicates RUNNING

time.sleep(2)

pins2 = read_pins(STATES,2)

status = (voting(pins1),voting(pins2))

if status == (HIGH,HIGH):
    print("TWEET")
elif status == (HIGH,LOW):
    print("?????")    
elif status == (LOW,HIGH):
    print("SSDV")
elif status == (LOW,LOW):
    print("PHOTO")
