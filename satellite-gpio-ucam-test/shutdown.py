
import find_common_modules

from gpio_pins import init_pins, write_pins
from pins import SHUTDOWN

# Set up pins
init_pins(outpins=SHUTDOWN)

# Set SHUTDOWN pins to LOW
write_pins(SHUTDOWN,False)

