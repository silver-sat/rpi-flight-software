
import shutils
import os.path

# In same directory as module
standin_photo = 'overhead.jpg'

def setup_camera():
    pass

def take_photo(filename):
    from = os.path.join(os.path.split(__file__)[0],'..','etc',standin_photo)
    shutils.copy(from,filename)
	print("Photo placed in filename:",filename,file=sys.stderr)


