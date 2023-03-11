
# Adapted from code written by Jalin
# https://github.com/silver-sat/payload2/blob/main/vote.py

# BCN numbers of STATES pins
SPIN1 = 16
SPIN2 = 20
SPIN3 = 21

STATES = [ SPIN1, SPIN2, SPIN3 ]

# BCN numbers of SHUTDOWN pins
DPIN1 = 17
DPIN2 = 27
DPIN3 = 22

SHUTDOWN = [ DPIN1, DPIN2, DPIN3 ]

# BCN numbers JUMPER pins
JPIN3 = 6
JPIN2 = 13
JPIN1 = 19
JPIN0 = 26

JUMPERS = [ JPIN0, JPIN1, JPIN2, JPIN3 ]

def pinstr(v):
    if v == True:
        return "HIGH"
    if v == False:
        return "LOW"
    if v == None:
        return "???"

