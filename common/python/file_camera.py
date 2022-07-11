
import shutil
import os, os.path, sys

photo_location = '/home/pi/.photo.jpg'

def setup_camera():
    pass

def take_photo(filename):
    if os.path.exists(photo_location):
        shutil.copyfile(photo_location,filename)
        print("Photo placed in filename:",filename,file=sys.stderr)
        return True
    return False
