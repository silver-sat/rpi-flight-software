
import find_common_modules

from gpio_pins import init_pins, write_pins
from pins import SERIALPIN, pinstr

import sys

# Select radio (default): True
# Select camera: False

setvalue = True
if len(sys.argv) >= 2:
    if sys.argv[1] == "RADIO":
        setvalue = True
    elif sys.argv[1] == "CAMERA":
        setvalue = False

# Set up pins
init_pins(outpins=[SERIALPIN])

# Set SERIALPIN pin
write_pins([SERIALPIN],setvalue)

print("Set SERIALPIN to",pinstr(setvalue))

