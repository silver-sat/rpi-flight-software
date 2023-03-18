
import os, os.path, sys

import RPi.GPIO as GPIO

from pins import JUMPERS, pinstr
from test_jumper import test_jumper

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

def read_pins(pins):
    j = test_jumpers(JUMPERS):
    if j == 1:
        return  [ None ] * len(pins)
    elif j == 2:
        return  [ False ] * len(pins)
    elif j == 3:
        return  [ True ] * len(pins)
    out = []
    for pin in pins:
        if GPIO.input(pin) == GPIO.HIGH:
            v = True
        else:
            v = False
        print("GPIO pin %d read as %s"%(pin,pinstr(v)),file=sys.stderr)
        out.append(v)
    return out
