
import find_common_modules
from file_pins import init_pins, write_pins
# from gpio_pins import init_pins, write_pins
from pins import SHUTDOWN

# Set SHUTDOWN pins to LOW
write_pins(SHUTDOWN,(False,False,False))

