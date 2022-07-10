
import os, os.path, sys, time

photo_dir = '/home/pi/photos'
photo_prefix = 'photo-'
photo_extn = '.jpg' # include dot!

def photo_filename():
    if not os.path.isdir(photo_dir):
        os.makedirs(photo_dir)
    # closest 1/10 second...
    t = int(round(10*time.time()))
    return "%s/%s%011d%s"%(photo_dir,photo_prefix,t,photo_extn)

def photo_sort_key(filename):
    # remove path
    fname = os.path.split(filename)[1]
    # remove prefix and extn
    fname = fname[len(photo_prefix):-len(photo_extn)]
    # remove prefix
    return int(fname)
                
def most_recent_photo():
    # so not rely on string sorting...
    globstr = photo_dir+"/" + photo_prefix + "*" + photo_extn
    for f in sorted(glob.glob(globstr),key=photo_sort_key):
        return f
    return None
                
def remove_photo(filename):
    if os.path.exists(filename):
        try:
            os.unlink(filename)
            print("Photo %s removed."%(os.path.split(filename)[1],),file=sys.stderr)
        except IOError:
            print("Photo %s removal failed."%(os.path.split(filename)[1],),file=sys.stderr)
    else:
        print("Photo %s not found."%(os.path.split(filename)[1],),file=sys.stderr)
    return
