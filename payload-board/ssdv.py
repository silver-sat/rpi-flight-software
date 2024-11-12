import serial
import time
import os

import find_common_modules

from photo_files import ssdv_filename, most_recent_photo
from kiss import kiss_encode

params = {}
for l in open("/home/pi/.params.sh"):
    k,v = map(lambda s: s.strip().strip(" '\""),l.split('='))
    params[k] = v

baud = int(params['BAUD'])
part_size = int(params['SSDVSIZE'])
sleep_time = float(params['SSDVDELAY'])
ssdv_time = int(params['SSDVTIME'])

photo_filename = most_recent_photo()
ssdvfn = ssdv_filename(photo_filename)

print("Sending photo file %s via SSDV"%(photo_filename,))
print("SSDV packets from %s"%(ssdvfn,))
print("BAUD: %d, SSDVSIZE: %d bytes, SSDVDELAY: %.2f sec, SSDVTIME: %d sec"%(baud,part_size,sleep_time,ssdv_time))

h = open(ssdvfn, "rb")
buffer = h.read()
h.close()

num_parts = len(buffer)//part_size
assert num_parts * part_size == len(buffer)

ser = serial.Serial('/dev/serial0', baud)
ser.reset_input_buffer()
ser.reset_output_buffer()

start_time = time.time()
end_time = start_time + ssdv_time

i=0; j=0;
while True:

    if time.time() > end_time:
        break

    part = buffer[i*part_size:(i+1)*part_size]
    ser.write(kiss_encode(part))

    i = (i+1)%num_parts
    j += 1

    time.sleep(sleep_time)

ser.close()
print("%d packets in image, %d packets sent, %.0f sec duration, packets sent %d times"%(num_parts,j,time.time()-start_time,j//num_parts))
