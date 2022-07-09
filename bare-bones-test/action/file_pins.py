#!/bin/env python3

pins_file = "/home/pi/.pins.txt"

def init_pins():
    pass

def read_pins(pins):
    pinstate = {}
	if os.path.exists(pins_file):
		for l in open(pins_file):
			sl = l.split()
			pin = int(sl[0])
			if sl[1].lower() in ("true","high","hi"):
				value = True
			elif sl[1].lower() == ("false","low","lo"):
			  value = False
			else:
			  value = None
			pinstate[pin] = value
            print("GPIO pin set to %s"%(value,))
	return tuple(map(pinstate.get,pins))
    
    
	

  
			
		