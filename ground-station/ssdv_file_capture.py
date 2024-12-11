# this script collects packets off the radio serial 0 (Payload) port and assembles them into a file

import serial
import argparse
import random
import copy
import binascii
import zipfile
from collections import defaultdict

def main(args):
    packets = dict()
    lastpacketnum = -1
    with serial.Serial('/dev/ttyS0', 9600, timeout=10) as ser:
        # print(ser.name)
        packet = bytearray(b'')
        packet_count = 0
        while True:
            x = ser.read(1)  # looking for C0
            # print(x)
            if x == b'\xc0':  # start of a packet detected
                dest = ser.read(1)  # read the destination (temp)
                # if args.verbose:
                #     print("dest = ", dest)
                packet = bytearray(b'')
                read_byte = None
                while read_byte not in (b'\xc0',b''):  # keep reading bytes until next 0xc0 encountered
                    read_byte = ser.read(1)  # need to kiss decode, do it on the fly
                    if read_byte == b'\xDB':
                        read_next_byte = ser.read(1)
                        if read_next_byte == b'\xDC':
                            packet.extend(b'\xC0')
                        elif read_next_byte == b'\xDD':
                            packet.extend(b'\xDB')
                    elif read_byte == b'\xc0':
                        pass
                    else:
                        packet.extend(read_byte)
            elif x == b'':
                break

            if packet != bytearray(b''):
                imagenum = int.from_bytes(packet[6:7],byteorder='big')
                packetnum = int.from_bytes(packet[7:9],byteorder='big')
                lastpacket = 1 if (int.from_bytes(packet[11:12],byteorder='big') & (1<<2)) else 0
                packetlen = len(packet)
                packetdata = packet[1:-4]
                calccrc = (binascii.crc32(packetdata) % (1<<32))
                packetcrc = (int.from_bytes(packet[-4:],byteorder='big') % (1<<32))
                if packetlen == 195 and calccrc == packetcrc:
                    packet_count += 1
                    print("len=",len(packet),end=" ")
                    print("image=",imagenum,end=" ")
                    print("packet=",packetnum,end=" ")
                    print("lastpacket=",lastpacket,end=" ")
                    print("packetcrc=",hex(packetcrc),end=" ")
                    print("calccrc=",hex(calccrc),end=" ")
                    print("count=",packet_count)
                    if packetnum not in packets:
                        packets[packetnum] = copy.copy(packet)
                        if lastpacket:
                            lastpacketnum = packetnum
                else:
                    print("Bad packet...")
                        
                packet = bytearray(b'') # clear it

            if len(packets) == 0:
                continue
            if min(packets) > 0:
                continue
            if lastpacketnum == -1 or len(packets) < (lastpacketnum + 1):
                continue
            break

    with open(args.output, "wb") as file:
        for i in sorted(packets):
            file.write(packets[i])
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ssdv_file_capture")
    parser.add_argument("-o", "--output", help="the file to write the received data")
    # parser.add_argument("-v", "--verbose", action="store_true", help="display packets")
    args = parser.parse_args()

    if args.output == None:
        print("output file required")
        quit()
    try:
        main(args)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Closing.")
