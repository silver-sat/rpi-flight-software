
from ..pins.file_pins import init_pins, read_pins
# from ..pins.gpio_pins import init_pins, read_pins
from ..pins.pins import STATES
from vote import voting

pins = read_pins(STATES)

assert None not in pins

if voting(pins):
   print "TWEET"
else
   print "PHOTO"