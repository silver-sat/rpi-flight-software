#!/bin/env python3

import os, os.path, sys

pins_file = "/home/pi/.pins.txt"

def init_pins():
    pass

def get_all_pins():
    pinstate = {}
    if os.path.exists(pins_file):
        for l in open(pins_file):
            if l.startswith('#'):
                continue
            sl = l.split()
            pin = int(sl[0])
            if sl[1].lower() in ("true","high","hi"):
                value = True
            elif sl[1].lower() in ("false","low","lo"):
                value = False
            else:
                value = None
            if value in (True,False):
                pinstate[pin] = value
                # print("GPIO pin %d read as %s"%(pin,"HIGH" if value else "LOW",))
    return pinstate

def write_all_pins(pinstate):
    wh = open(pins_file,'w')
    for p,v in sorted(pinstate.items()):
        if v in (True,False):
            v = 'HIGH' if v else 'LOW'
            print(f"{p}\t{v}",file=wh)
    wh.close()

def write_pins(pins,values):
    pinstate = get_all_pins()
    for p,v in sorted(zip(pins,values)):
        pinstate[p] = v
        print("GPIO pin %d set to %s"%(p,"HIGH" if v else "LOW",),file=sys.stderr)
    write_all_pins(pinstate)

def read_pins(pins):
    pinstate = get_all_pins()   
    for pin in pins:
        print("GPIO pin %d read as %s"%(pin,"HIGH" if pinstate[pin] else "LOW",),file=sys.stderr)
    return tuple(map(pinstate.get,pins))
