
import sys

import find_common_modules

from photo_files import photo_filename, thumb_filename, ssdv_filename
from photo_thumb import make_thumb
from photo_ssdv import make_ssdv

from file_camera import file_photo_is_present
if file_photo_is_present():
    from file_camera import setup_camera, take_photo
else:
    from ucam_serial_camera import setup_camera
    from ucam_take_photo import take_photo

camera = setup_camera()

filename = photo_filename()
if not filename:
    print("Can't generate a new photo filename, too many photos",file=sys.stderr)
    sys.exit(1)

thumbfn = thumb_filename(filename)
ssdvfn = ssdv_filename(filename)

if take_photo(camera, filename):
    make_thumb(2,filename,thumbfn)
    make_ssdv(thumbfn,ssdvfn)
    print("Success!",file=sys.stderr)
    
