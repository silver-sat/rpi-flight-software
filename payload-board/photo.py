
import sys

import find_common_modules

from photo_files import photo_filename, thumb_filename, ssdv_filename
from photo_thumb import make_thumb
from photo_ssdv import make_ssdv

#
# Choose the camera module for file, ucam_max3100, or ucam_serial
#
# from file_camera import setup_camera
# from ucam_max3100_camera import setup_camera
from ucam_serial_camera import setup_camera

#
# Match the take_photo module with the above
#
# from file_camera import take_photo
from ucam_take_photo import take_photo

camera = setup_camera()

filename = photo_filename()
thumbfn = thumb_filename(filename)
ssdvfn = ssdv_filename(filename)

if take_photo(camera, filename):
    make_thumb(2,filename,thumbfn)
    make_ssdv(thumbfn,ssdvfn)
    print("Success!",file=sys.stderr)
    