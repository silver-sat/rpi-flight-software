
import find_common_modules

from photo_files import photo_filename
from ucam_serial_camera import setup_camera
from ucam_take_photo import take_photo

import traceback
import sys
import time

delay_time = 60
last_photo_time = 0
start = time.time()

while True:

    if (time.time()-last_photo_time) < delay_time:
        time.sleep(max(0,delay_time-(time.time()-last_photo_time)))
    last_photo_time = time.time()

    print("Time since start: %.0f sec."%(time.time()-start,),file=sys.stderr)

    try:
        camera = setup_camera()
        filename = photo_filename()
        take_photo(camera, filename)
    except:
        traceback.print_exc()

