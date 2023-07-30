
import sys

import find_common_modules

from photo_files import photo_filename

#
# Choose the camera module for file, ucam_max3100, or ucam_serial
#
# from file_camera import setup_camera
from ucam_max3100_camera import setup_camera
# from ucam_serial_camera import setup_camera

#
# Match the take_photo module with the above
#
# from file_camera import take_photo
from ucam_take_photo import take_photo

camera = setup_camera()

filename = photo_filename()

if take_photo(camera, filename):
    print("Success!",file=sys.stderr)
    