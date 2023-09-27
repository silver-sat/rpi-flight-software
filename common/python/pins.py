
# Adapted from code written by Jalin
# https://github.com/silver-sat/payload2/blob/main/vote.py

# BCM numbers of STATES pins
SPIN1 = 16 # physical pin 36
SPIN2 = 20 # physical pin 38
SPIN3 = 21 # physical pin 40

STATES = [ SPIN1, SPIN2, SPIN3 ]

# BCM numbers of SHUTDOWN pins
DPIN1 = 17 # physical pin 11
DPIN2 = 27 # phyiscal pin 13
DPIN3 = 22 # phyiscal pin 15

SHUTDOWN = [ DPIN1, DPIN2, DPIN3 ]

# BCM number serial switch pin
SERIALPIN = 5 # physical pin 29

# BCM numbers JUMPER pins
JPIN3 = 6  # physical pin 31
JPIN2 = 13 # physical pin 33
JPIN1 = 19 # physical pin 35
JPIN0 = 26 # physical pin 37

JUMPERS = [ JPIN0, JPIN1, JPIN2, JPIN3 ]

def pinstr(v):
    if v == True:
        return "HIGH"
    if v == False:
        return "LOW"
    if v == None:
        return "???"

