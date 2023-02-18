
# Based on code by Dave Copeland and Xander Hostler

import serial
import time, os, os.path, math, sys
import RPi.GPIO as GPIO

class uCAM_III(object):

    # BCM number for reset pin on GPIO header
    default_resetPin = 23
    # time to wait before reading camera response
    default_responseDelay = 1
    # time to wait for reading camera response to sync
    default_syncResponseDelay = 1
    # time to wait between commands
    default_interCommandDelay = 1
    # time to wait for a response to a command (after the repsonseDelay)
    default_responseTimeout = 1
    # JPG size (see below)
    default_jpgSize = 3

    # uCAM III protocol...
    INITIAL = (0xAA,0x01,0x00,0x00,0x00,0x00)
    INITIAL_JPEG_1 = (0xAA,0x01,0x00,0x07,0x07,0x03)  # 160x128 format      
    INITIAL_JPEG_2 = (0xAA,0x01,0x00,0x07,0x07,0x05)  # 320x240 format      
    INITIAL_JPEG_3 = (0xAA,0x01,0x00,0x07,0x07,0x07)  # 640x480 format      
    SNAPSHOT = (0xAA,0x05,0x00,0x00,0x00,0x00)
    GETPICTURE = (0xAA,0x04,0x01,0x00,0x00,0x00)
    FULL_RESET = (0xAA,0x08,0x00,0x00,0x00,0x00)
    SYNC = (0xAA,0x0D,0x00,0x00,0x00,0x00)
    ACK = (0xAA,0x0E)
    LIGHT = (0xAA,0x13,0x01,0x00,0x00,0x00)
    EXPSETTINGS = (0xAA,0x14,0x02,0x02,0x02,0x00)

    BAUD_9600 = (0xAA,0x07,0x1F,0x0B,0x00,0x00)
    # 57600 in data-sheet
    BAUD_56000 = (0xAA,0x07,0x1F,0x01,0x00,0x00)

    PKGSIZE_512 = (0xAA,0x06,0x08,0x00,0x02,0x00)
    PKGSIZE_256 = (0xAA,0x06,0x08,0x00,0x01,0x00)
    PKGSIZE_128 = (0xAA,0x06,0x08,0x80,0x00,0x00)
    PKGSIZE_64  = (0xAA,0x06,0x08,0x40,0x00,0x00)

    def __init__(self,**kw):
        self.resetPin = kw.get('resetPin',self.default_resetPin)
        self.responseDelay = kw.get('responseDelay',self.default_responseDelay)
        self.responseTimeout = kw.get('responseTimeout',self.default_responseTimeout)
        self.syncResponseDelay = kw.get('syncResponseDelay',self.default_syncResponseDelay)
        self.interCommandDelay = kw.get('interCommandDelay',self.default_interCommandDelay)
        self.jpgSize = kw.get('jpgSize',self.default_jpgSize)
        self.verbose = kw.get('verbose',False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.resetPin,GPIO.OUT)

    def reset(self):
        GPIO.output(self.resetPin,GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.resetPin,GPIO.HIGH)

    def full_reset(self):
        self.command(self.FULL_RESET)

    def command(self,bytes,**kw):
        responseDelay = kw.get('responseDelay',self.responseDelay)
        responseTimeout = kw.get('responseTimeout',self.responseTimeout)
        verbose=kw.get('verbose',self.verbose)
        wait=kw.get('wait',True)
        verify=kw.get('verify',False)
        expectedLen = kw.get('expectedLen',1)
        if verbose:
            print("Write:",len(bytes),":"," ".join(map(lambda b: "%02X"%b,bytes)),file=sys.stderr)
        self.write(bytes)
        time.sleep(responseDelay)
        timeout = time.time()+responseTimeout
        retval = self.read()
        while wait and len(retval) < expectedLen and time.time()<timeout:
            retval += self.read()
        if verbose:
            print("Read: ",len(retval),":"," ".join(map(lambda b: "%02X"%b,retval)),file=sys.stderr)
        if verify:
            self.check_ack(retval,bytes[1])
        return retval

    def check_ack(self,reply,cmd):
        return tuple(map(int,reply[:3])) == (0xAA,0x0E,cmd)

    def check_sync_ack(self,reply):
        return self.check_ack(reply,0x0D)

    def sync(self,**kw):
        syncResponseDelay = kw.get('syncResponseDelay',self.syncResponseDelay)
        maxTries = 60
        currentTry = 0
        reply = b''
        delayValue = 0.005
        delayIncrement = 0.001
    
        while (currentTry < maxTries) and (len(reply) != 12 or not self.check_sync_ack(reply[:6])):
            # print("Sync attempt:",currentTry)
            delayValue += delayIncrement
            reply = self.command(self.SYNC, responseDelay=syncResponseDelay, wait=False)
            currentTry +=1

        if len(reply) != 12 or not self.check_sync_ack(reply[:6]):
            # Didn't work
            if self.verbose:
                print("Sync didn't work. Sent %d tries" % currentTry,file=sys.stderr)
            return False

        # it did work
        if self.verbose:
            print("Camera replied", " ".join(map(lambda b: "%02X"%b,reply)), "attempts:",currentTry,file=sys.stderr)
        
        # send the ACK back to camera        
        self.sendack(reply[6:][1])
        return True

    def sendack(self,cmd):
        bytes = self.ACK+(cmd,0x00,0x00,0x00)
        if self.verbose:
            print("Write:",len(bytes),":"," ".join(map(lambda b: "%02X"%b,bytes)),file=sys.stderr)
        self.write(bytes)

    def check_sync(self):
        reply = self.command(self.SYNC)
        if len(reply) != 12 or not self.check_sync_ack(reply[:6]):
            return False
        self.sendack(reply[6:][1])
        return True

    def set_jpg(self,size):
        jpg_const = "INITIAL_JPEG_%s"%(size,)
        assert hasattr(self,jpg_const), "No uCAM_III.%s constant"%(jpg_const,)
        reply = self.command(getattr(self,jpg_const))
        assert self.check_ack(reply,self.INITIAL_JPEG_1[1])

    def set_baud(self,baud):
        baud_const = "BAUD_%s"%(baud,)
        assert hasattr(self,baud_const), "No uCAM_III.%s constant"%(baud_const,)
        reply = self.command(getattr(self,baud_const),expectedLen=6)
        assert self.check_ack(reply,self.BAUD_9600[1])

    def set_package_size(self,size):
        size_const = "PKGSIZE_%s"%(size,)
        assert hasattr(self,size_const), "No uCAM_III.%s constant"%(size_const,)
        reply = self.command(getattr(self,size_const))
        assert self.check_ack(reply,self.PKGSIZE_512[1])

    def takephoto(self):
        time.sleep(self.interCommandDelay)
        self.set_jpg(self.jpgSize)
        time.sleep(self.interCommandDelay)
        self.set_package_size(self.pkgSize)
        time.sleep(self.interCommandDelay)
        self.command(self.EXPSETTINGS,verify=True)
        time.sleep(self.interCommandDelay)
        self.command(self.SNAPSHOT,verify=True)

    def retrieveDataFromPkg(self,pkg):
        # pkgID = pkg[0:2]
        dataBuffer = pkg[4:-2]
        return dataBuffer

    def getPictureSize(self):
        response = self.command(self.GETPICTURE)
        print("Wrote GETPICTURE. Camera replied",response,file=sys.stderr)
        return response[-1]*256*256+response[-2]*256+response[-3]

    def getPicture(self):
        pictureArray = None
        imageSize = None
        numPackages = None
        goodpkg = 0
        for attempt in range(0,10):
            camReply = self.command(self.GETPICTURE)
            # print("Wrote GETPICTURE. Camera replied",camReply)
            i = 0
            while len(camReply) < 12 and i < 5: # ACK + DATA command response
                camReply += self.read()
                i += 1
            if self.verbose:
                print("Read: ",len(camReply),":"," ".join(map(lambda b: "%02X"%b,camReply)),file=sys.stderr)
            if len(camReply) < 12:
                time.sleep(5)
                continue
                
            if imageSize == None:
                replyLen=len(camReply)
                imageSize = camReply[replyLen-1]*256*256+camReply[replyLen-2]*256+camReply[replyLen-3]
                print("Picture size:",imageSize,"bytes")
                numPackages = int(math.ceil(imageSize/(self.pkgSize-6)))
                pictureArray = [b'']*numPackages

            for indx in range(numPackages):
                ackResponse = self.ACK+(0,0,indx,0)
                if indx < (numPackages-1):
                    expectedLen = self.pkgSize
                else:
                    expectedLen = imageSize-(numPackages-1)*(self.pkgSize-6)+6
                pkg = self.command(ackResponse,expectedLen=expectedLen)
                pkgID0 = pkg[0]
                pkgID1 = pkg[1]
                pkgdatalen = pkg[2]+256*pkg[3]
                pkgverify = pkg[-2]
                verify = (sum(pkg[:-2])&0xff)
                   
                if pkgID0 == (indx+1) and pkgverify == verify and len(pkg) == expectedLen and (pkgdatalen+6) == expectedLen:
                    if pictureArray[indx] == b"":
                        pictureArray[indx] = self.retrieveDataFromPkg(pkg)
                        goodpkg += 1
                        print("Received package %3d (%3d/%3d): %6.2f%% (pass %d)" % (indx+1,goodpkg,numPackages,100.0*goodpkg/numPackages,attempt+1),file=sys.stderr)
                        if goodpkg == numPackages:
                            break
                else:
                    pass # print("Bad package %d %d - exp. size %d, actual size %d, pkgvfy %d, sumvfy: %d" % (indx+1,pkgID0,expectedLen,len(pkg),pkgverify,verify))
                # time.sleep(self.interCommandDelay)

            bytes = self.ACK+(0,0,0xF0,0xF0)
            if self.verbose:
                print("Write:",len(bytes),":"," ".join(map(lambda b: "%02X"%b,bytes)),file=sys.stderr)
            self.write(bytes)

            if goodpkg == numPackages:
                break

        assert goodpkg == numPackages

        pictureArray = b''.join(pictureArray)
        print("Received - %d/%d  bytes" % (imageSize,len(pictureArray)),file=sys.stderr)
        return pictureArray

    def savePicture(self,filename):
        print("Picture filename:",filename,file=sys.stderr)
        start = time.time()
        picture = self.getPicture()
        print("Picture size:",len(picture),file=sys.stderr)
        picFile = open(filename,'wb')
        picFile.write(picture)
        picFile.close()
        print("Time to save: %0f sec"%(time.time()-start,),file=sys.stderr)

class uCAM_III_Serial(uCAM_III):
    # Constants
    default_baudRate = 56000
    pkgSize = 512

    # initialize
    def __init__(self,serialDevice,**kw):
        self.baudRate = kw.get('baudRate',self.default_baudRate)
        self.serialPort = serial.Serial(serialDevice,self.baudRate)
        super(uCAM_III_Serial,self).__init__(**kw)

    def read(self):
        readString = b''
        bytesToRead = self.serialPort.in_waiting
        while bytesToRead >0:
            readByte= self.serialPort.read(1)
            readString += readByte
            bytesToRead = self.serialPort.in_waiting
            time.sleep(0.00005)
        return readString

    def write(self,bytes):
        self.serialPort.write(bytes)

import pymax3100

class uCAM_III_MAX3100(uCAM_III):
    # Constants
    default_baudRate = 9600
    pkgSize = 512

    # initialize
    def __init__(self,spiDevice,**kw):
        self.baudRate = kw.get('baudRate',self.default_baudRate)
        # other MAX3100 parameters are set to default values
        self.max3100 = max3100.MAX3100(spiif=spiDevice[0],
                                       spiselect=spiDevice[1],
                                       baud=self.baudRate)
        super(uCAM_III_MAX3100,self).__init__(**kw)

    def read(self):
        return self.max3100.readbytes()

    def write(self,bytes):
        self.max3100.writebytes(bytes)




