
import find_common_modules

from photo_files import photo_filename
from ucam_serial_camera import setup_camera
# reimplemented below to enable LED
# from ucam_take_photo import take_photo
from gpio_pins import init_pins, write_pins

import traceback
import sys
import time

LEDPIN=[24,]

init_pins(outpins=LEDPIN)
write_pins(LEDPIN,False)

delay_time = 90
last_photo_time = 0
start = time.time()

while True:

    if (time.time()-last_photo_time) < delay_time:
        time.sleep(max(0,delay_time-(time.time()-last_photo_time)))
    last_photo_time = time.time()

    print("Time since start: %.0f sec."%(time.time()-start,),file=sys.stderr)

    camera = setup_camera()
    filename = photo_filename()

    # from take_photo
    attempt = 0
    while True:
        print("Connect w/ camera, attempt",attempt+1,file=sys.stderr)
        attempt += 1
        camera.reset()
        try:
            camera.sync()
        except:
            time.sleep(1)
            continue
        try:
            camera.set_baud(camera.baudRate)
        except:
            time.sleep(1)
            continue
        break
        
    time.sleep(2)

    write_pins(LEDPIN,True)
    camera.takephoto()
    write_pins(LEDPIN,False)

    time.sleep(2)

    print("Save photo",file=sys.stderr)

    try:
        camera.savePicture(filename)
        print("Photo placed in filename:",filename,file=sys.stderr)
    except:
        traceback.print_exc()

