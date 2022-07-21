#!/bin/env python3

import spidev
import serial
import sys
import time
import array
import itertools
import hashlib
import random

class MAX3100(object):

    # Commands.
    CMD_WRITE_CONF      = 0b1100000000000000
    CMD_READ_CONF       = 0b0100000000000000
    CMD_WRITE_DATA      = 0b1000000000000000
    CMD_READ_DATA       = 0b0000000000000000
    
    # Configuration.
    CONF_R              = 0b1000000000000000
    CONF_T              = 0b0100000000000000
    CONF_RM             = 0b0000010000000000

    # Baud rates for clock multiplier x1.
    CONF_BAUD_X1_115200 = 0b0000000000000000
    CONF_BAUD_X1_57600  = 0b0000000000000001
    CONF_BAUD_X1_38400  = 0b0000000000001000
    CONF_BAUD_X1_19200  = 0b0000000000001001
    CONF_BAUD_X1_9600   = 0b0000000000001010
    CONF_BAUD_X1_4800   = 0b0000000000001011
    CONF_BAUD_X1_2400   = 0b0000000000001100
    CONF_BAUD_X1_1200   = 0b0000000000001101
    CONF_BAUD_X1_600    = 0b0000000000001110
    CONF_BAUD_X1_300    = 0b0000000000001111
    
    # Baud rates for clock multiplier x2.
    CONF_BAUD_X2_230400 = 0b0000000000000000
    CONF_BAUD_X2_115200 = 0b0000000000000001
    CONF_BAUD_X2_57600  = 0b0000000000000010
    CONF_BAUD_X2_38400  = 0b0000000000001001
    CONF_BAUD_X2_19200  = 0b0000000000001010
    CONF_BAUD_X2_9600   = 0b0000000000001011
    CONF_BAUD_X2_4800   = 0b0000000000001100
    CONF_BAUD_X2_2400   = 0b0000000000001101
    CONF_BAUD_X2_1200   = 0b0000000000001110
    CONF_BAUD_X2_600    = 0b0000000000001111

    CRYSTAL_1843_kHz = 1
    CRYSTAL_3686_kHz = 2

    def __init__(self,spiif=0,spiselect=0,spispeed=7800000,
                      crystal_kHz=3686,baud=9600):
        crystal_const = "CRYSTAL_%s_kHz"%(crystal_kHz,)
        assert hasattr(self,crystal_const), "No MAX3100.%s constant"%(crystal_const,)
        self.crystal = getattr(self,crystal_const)
                
        self.spi = spidev.SpiDev()
        self.spi.open(spiif,spiselect)
        self.spi.max_speed_hz = spispeed
        self.spi.mode = 0b00

        self.set_baud(baud)

    @staticmethod
    def tobytearray(words):
        msws = map(lambda w: (w&0xffff)>>8, words)
        lsws = map(lambda w: (w&0xff), words)
        return array.array('B',[ item for pair in zip(msws,lsws) for item in pair ])

    @staticmethod
    def frombytearray(bytes):
        return [ (bytes[i]<<8 | bytes[i+1]) for i in range(0,len(bytes),2) ]
        
    def tobytelist(self,word):
        return [ (word&0xffff)>>8, word&0xff ]

    def frombytelist(self,bytelist):
        return (bytelist[0]<<8 | bytelist[1])

    def xferword(self,word,msg=None):
        if msg:
            self.print_word(msg+":send",word)
        rword = self.frombytelist(self.spi.xfer(self.tobytelist(word)))
        if msg:
            self.print_word(msg+":read",rword)
        return rword

    def set_baud(self,baud):
        baud_const = "CONF_BAUD_X%s_%s"%(self.crystal,baud)
        assert hasattr(self,baud_const), "No MAX3100.%s constant"%(baud_const,)
        conf = getattr(self,baud_const)
        word = ( self.CMD_WRITE_CONF | self.CONF_RM | conf )
        self.xferword(word)

    readcmd = tobytearray.__func__([CMD_READ_DATA])
    def readbytes(self):
        byteslist = []
        while True:
            bytesi = list(filter(lambda t: t[0]&0x80,( self.spi.xfer(self.readcmd) for _ in range(128))))
            if len(bytesi) == 0:
                break           
            byteslist.extend(bytesi)
        return bytes(t[1] for t in byteslist)

    def read(self):
        r = self.xferword(self.CMD_READ_DATA)
        if r&self.CONF_R:
            return r&0xff
        return None

    def available(self):
        r = self.xferword(self.CMD_READ_CONF)
        return bool(r&self.CONF_R)

    def write(self,byte):
        while True:
            if not self._busy():
                r = self.xferword((self.CMD_WRITE_DATA | (byte & 0xff)))
                break
        return True

    def _busy(self):
        r = self.xferword(self.CMD_READ_CONF)
        return (not (r & self.CONF_T))

    readconf = tobytearray.__func__([CMD_READ_CONF])
    writecmd = tobytearray.__func__([CMD_WRITE_DATA])
    def writebytes(self,buffer):
        for b in buffer: 
            self.writecmd[1] = b
            while True:
                # (return_value & CONF_T)
                if self.spi.xfer(self.readconf)[0]&0x40:
                    break
            self.spi.xfer(self.writecmd)

    def print_word(self,prefix,word,file=sys.stderr):
        binstr = bin(word)[2:]
        binstr = (16-len(binstr))*'0' + binstr
        binstr = " ".join([binstr[:8],binstr[8:]])
        chr1 = chr(word>>8) if (33 <= (word>>8) <= 126) else "?"
        chr2 = chr(word&0xff) if (33 <= (word&0xff) <= 126) else "?"
        hexstr = hex(word)[2:].upper()
        hexstr = (4-len(hexstr))*'0' + hexstr
        print('%s: bin:%s hex:%s chr:%s%s'%(prefix,binstr,hexstr,chr1,chr2),file=file)


if __name__ == "__main__":

    # MAX3100 Loop-back via Serial Port test...

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


    def serial_thread(baud,length):
        time.sleep(1)
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

    p1 = Process(target=serial_thread,args=(serial_baud,length))
    p1.start()

    p2 = Process(target=max3100_thread,args=(serial_baud,length))
    p2.start()

    p1.join()
    p2.join()

