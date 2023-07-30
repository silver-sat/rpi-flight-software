
import find_common_modules

from gpio_pins import init_pins, write_pins
from pins import SHUTDOWN

import sys

setvalue = False
if len(sys.argv) >= 2:
    if sys.argv[1] == "RUNNING":
        setvalue = False
    elif sys.argv[1] == "FINISHED":
        setvalue = True

# Set up pins
init_pins(outpins=SHUTDOWN)

# Set SHUTDOWN pins to LOW
write_pins(SHUTDOWN,setvalue)

