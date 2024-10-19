
import os, os.path, sys

import RPi.GPIO as GPIO

from pins import JUMPERS, pinstr
from test_jumper import test_jumpers

def init_pins(inpins=[],outpins=[]):

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    for pin in inpins:
        GPIO.setup(pin, GPIO.IN)
    for pin in outpins:
        GPIO.setup(pin, GPIO.OUT)
        
    return

def write_pins(pins,values):
    if values in (True,False):
        values = [values]*len(pins)
    for p,v in sorted(zip(pins,values)):
        if v not in (True,False):
            continue
        GPIO.output(p,GPIO.HIGH if v else GPIO.LOW)
        print("GPIO pin %d set to %s"%(p,pinstr(v)),file=sys.stderr)
    return

def read_pins(pins, step=1):
    j = test_jumpers(JUMPERS)
    if j == 1:
        print("GPIO JUMPERS 1 (None)",file=sys.stderr)
        return  [ None ] * len(pins)
    elif j == 2:
        print("GPIO JUMPERS 2 (False)",file=sys.stderr)
        return  [ False ] * len(pins)
    elif j == 3:
        print("GPIO JUMPERS 3 (True)",file=sys.stderr)
        return  [ True ] * len(pins)
    elif j == 4: #SSDV
        if step == 1:
            print("GPIO JUMPERS 4 (True)",file=sys.stderr)
            return  [ True ] * len(pins)
        elif step == 2:
            print("GPIO JUMPERS 4 (False)",file=sys.stderr)
            return  [ False ] * len(pins)
    out = []
    for pin in pins:
        if GPIO.input(pin) == GPIO.HIGH:
            v = True
        else:
            v = False
        print("GPIO pin %d read as %s"%(pin,pinstr(v)),file=sys.stderr)
        out.append(v)
    return out
