#!/bin/env python3

import spidev
import serial
import sys
import time
import array
import itertools
import hashlib
import random

import find_common_modules

from max3100 import MAX3100

# MAX3100 Loop-back via Serial Port test...
# Or separate programs on different rPIs....
from multiprocessing import Process

def max3100_thread(baud,length):
    max3100 = MAX3100(baud=baud)
    while True:
        start = time.time()
        bytes = max3100.readbytes()
        if len(bytes) > 0:
            break
    print("%4d characters (%s) received (SPI) in %f seconds"%(len(bytes),hashlib.md5(bytes).hexdigest().lower(),time.time()-start))

    time.sleep(2)

    print("%4d characters (%s) to send (SPI)"%(len(bytes),hashlib.md5(bytes).hexdigest().lower()))
    max3100.writebytes(bytes)

    time.sleep(2)

    while True:
        bytes = "".join(chr(ord('A')+random.randint(0,25)) for i in range(0,6)).encode('utf8')
        print("%4d characters (%s) to send (SPI)"%(len(bytes),bytes))
        max3100.writebytes(bytes)
        bytes = max3100.readbytes()
        print("%4d characters (%s) received (SPI)"%(len(bytes),bytes))
        time.sleep(1)


def serial_thread(baud,length,delay):
    time.sleep(delay)
    ser = serial.Serial('/dev/serial0',baud)
    ser.reset_output_buffer()
    ser.reset_input_buffer()
    str = "".join(chr(ord('A')+random.randint(0,25)) for i in range(0,length))
    print("%4d characters (%s) to send (serial,%d baud)"%(len(str),hashlib.md5(str.encode('utf8')).hexdigest().lower(),baud))
    ser.write(str.encode('utf8'))
    time.sleep(0.1)
    while ser.in_waiting == 0:
        pass
    start = time.time()
    str = ser.read(length).decode('utf8')
    print("%4d characters (%s) received (serial) in %f seconds"%(len(str),hashlib.md5(str.encode('utf8')).hexdigest().lower(),time.time()-start))
    time.sleep(1)
    while True:
        bytes = ser.read(6)
        ser.write(bytes)

    ser.close()
    time.sleep(1)

serial_baud = 38400
length = 1024

if sys.argv[1] == "serial":
    serial_thread(serial_baud,length,5)
elif sys.argv[1] == "max3100":
    max3100_thread(serial_baud,length)
elif sys.argv[1] == "both":
    p1 = Process(target=serial_thread,args=(serial_baud,length,1))
    p1.start()

    p2 = Process(target=max3100_thread,args=(serial_baud,length))
    p2.start()

    p1.join()
    p2.join()
else:
    print("Please indicate: \"serial\", \"max3100\", or \"both\".")
