
import shutil
import os, os.path, sys

# In same directory as module
standin_photo = 'overhead.jpg'

def setup_camera():
    pass

def take_photo(filename):
    photo = os.path.join(os.path.split(__file__)[0],'..','etc',standin_photo)
    shutil.copyfile(photo,filename)
    print("Photo placed in filename:",filename,file=sys.stderr)


