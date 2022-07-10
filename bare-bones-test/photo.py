
import find_common_modules

from photo_files import photo_filename
from file_camera import setup_camera, take_photo

setup_camera()

filename = photo_filename()

if take_photo(filename):
    print("Success!",file=sys.stderr)
    