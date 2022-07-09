#!/bin/env python3

pins_file = "/home/pi/.pins.txt"

def init_pins():
    pass

def get_all_pins():
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
            print("GPIO pin %d read as %s"%(pin,"HIGH" if value else "LOW",))
    return pinstate

def write_all_pins(pinstate):
    wh = open(pins_file,'w')
    for p,v in sorted(pinstate):
        print(f"{p}\t{'HIGH' if v else 'LOW'}",file=wh)
    wh.close()

def write_pins(pins,values):
    pinstate = get_all_pins()
    for p,v in zip(pins,values):
        pinstate[p] = v
        print("GPIO pin set to %s"%(p,"HIGH" if v else "LOW",))
    write_all_pins(pinstate)

def read_pins(pins):
    pinstate = get_all_pins()   
	return tuple(map(pinstate.get,pins))
    
    
	

  
			
		