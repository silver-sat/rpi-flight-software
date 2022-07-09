
from ..pins.file_pins import init_pins, write_pins
# from ..pins.gpio_pins import init_pins, write_pins
from ..pins.pins import SHUTDOWN

# Set SHUTDOWN pins to LOW
write_pins(SHUTDOWN,(False,False,False))

