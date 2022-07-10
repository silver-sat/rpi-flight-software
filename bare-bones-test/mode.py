
import find_common_modules

from file_pins import init_pins, read_pins
from pins import STATES
from vote import voting

# initialize pins
init_pins()

# read STATES pins
pins = read_pins(STATES)

if None not in pins:
    if voting(pins):
        print("TWEET")
    else:
        print("PHOTO")
