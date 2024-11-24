# this script collects packets off the radio serial 0 (Payload) port and assembles them into a file

import serial
import argparse

def main(args):
    with serial.Serial('/dev/ttyS0', 9600) as ser:
        print(ser.name)
        packet = []
        packet_count = 0
        while True:
            x = ser.read(1)  # looking for C0
            # print(x)
            if x == b'\xc0':  # start of a packet detected
                dest = ser.read(1)  # read the destination (temp)
                if args.verbose:
                    print("dest = ", dest)
                packet = bytearray(b'')
                read_byte = None
                while read_byte != b'\xc0':  # keep reading bytes until next 0xc0 encountered
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

            if args.verbose:
                print(packet)
                print(len(packet))
            with open(args.output, "ab") as file:  #append to the file
                file.write(packet)
            packet_count += 1
            packet = []  # clear it
            print(f'count = {packet_count}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="ssdv_file_capture")
    parser.add_argument("-o", "--output", help="the file to write the received data")
    parser.add_argument("-v", "--verbose", action="store_true", help="display packets")
    args = parser.parse_args()

    if args.output == None:
        print("output file required")
        quit()
    try:
        main(args)
    except KeyboardInterrupt:
        print("Keyboard interrupt. Closing.")