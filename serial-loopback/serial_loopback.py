#!/bin/env python3

import serial
import sys
import time
import array
import itertools
import hashlib
import random

serial_baud = 9600
length = 1024
    
# open serial
ser = serial.Serial('/dev/serial0',baud)
ser.reset_output_buffer()
ser.reset_input_buffer()

# random string
str = "".join(chr(ord('A')+random.randint(0,25)) for i in range(0,length))

# length and hash
prstr = str
if len(prstr) > 10:
    prstr = str[:4]+".."+str[-4:]
print("%4d characters (%s,%s) to send (serial,%d baud)"%(len(str),prstr,hashlib.md5(str.encode('utf8')).hexdigest().lower(),baud))

# write to serial
ser.write(str.encode('utf8'))
time.sleep(0.1)

# Wait for a character
while ser.in_waiting == 0:
    pass
    
# start timer
start = time.time()

# read string
str = ser.read(length).decode('utf8')

# print length and hash
prstr = str
if len(prstr) > 10:
    prstr = str[:4]+".."+str[-4:]
print("%4d characters (%s,%s) received (serial) in %f seconds"%(len(str),prstr,hashlib.md5(str.encode('utf8')).hexdigest().lower(),time.time()-start))

# close serial 
ser.close()

