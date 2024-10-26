# import find_common_modules
import serial
import time
import os

# from photo_files import ssdv_filename, most_recent_photo


baud = int(os.environ['BAUD'])
part_size = int(os.environ['SSDVSIZE'])
sleep_time = float(os.environ['SSDVDELAY'])
ssdv_time = int(os.environ['SSDVTIME'])

# photo_filename = most_recent_photo()
# ssdvfn = ssdv_filename(photo_filename)
ssdvfn = "ssdv-000001.bin"

h = open(ssdvfn, "rb")
buffer = h.read()
h.close()


num_parts = len(buffer)//part_size
assert num_parts * part_size == len(buffer)

# ssdv_time = num_parts*sleep_time*2

ser = serial.Serial('/dev/pts/5', baud)
ser.reset_input_buffer()
ser.reset_output_buffer()

start_time = time.time()
end_time = start_time + ssdv_time

i=0
while True:
    if time.time() > end_time:
        break

    
    part = buffer[i*part_size:(i+1)*part_size]
    
    ser.write(part)

    i+=1
    if i == num_parts:
        i=0

    time.sleep(sleep_time)


ser.close()

