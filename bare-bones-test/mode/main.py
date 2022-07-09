
import find_common_modules

from file_pins import init_pins, read_pins
# from gpio_pins import init_pins, read_pins
from pins import STATES
from vote import voting

pins = read_pins(STATES)

assert None not in pins

if voting(pins):
   print("TWEET")
else:
   print("PHOTO")
