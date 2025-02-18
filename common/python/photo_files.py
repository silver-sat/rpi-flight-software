
import os, os.path, sys, time, glob

photo_dir = os.path.join(os.path.expanduser("~"),'photos')
photo_prefix = 'photo-'
photo_extn = '.jpg' # include dot!
thumb_prefix = 'thumb-'
thumb_extn = '.jpg'
ssdv_prefix = 'ssdv-'
ssdv_extn = '.bin'

# def photo_filename():
# if not os.path.isdir(photo_dir):
# os.makedirs(photo_dir)
# # closest 1/10 second...
# t = int(round(10*time.time()))
# return "%s/%s%011d%s"%(photo_dir,photo_prefix,t,photo_extn)
    
last_photo_index_filename = photo_dir+"/last_photo_index.txt"

def photo_filename():
    globstr = photo_dir+"/" + photo_prefix + "*" + photo_extn
    if len(list(glob.glob(globstr))) > 20:
        return None
    if os.path.exists(last_photo_index_filename):
        last_photo_index = int(open(last_photo_index_filename).read())  
    else:
        last_photo_index = 0
    last_photo_index += 1
    filename = "%s/%s%06d%s"%(photo_dir,photo_prefix,last_photo_index,photo_extn)
    wh = open(last_photo_index_filename,'w')
    wh.write(str(last_photo_index)+"\n")
    wh.close()
    return filename

def thumb_filename(photo_filename):
    index = photo_sort_key(photo_filename)
    return "%s/%s%06d%s"%(photo_dir,thumb_prefix,index,thumb_extn)

def ssdv_filename(photo_filename):
    index = photo_sort_key(photo_filename)
    return "%s/%s%06d%s"%(photo_dir,ssdv_prefix,index,ssdv_extn)

def photo_sort_key(filename):
    if filename == None:
        return 0
    # remove path
    fname = os.path.split(filename)[1]
    # remove prefix and extn
    fname = fname[len(photo_prefix):-len(photo_extn)]
    # remove prefix
    return int(fname)
                
def most_recent_photo():
    # so not rely on string sorting...
    globstr = photo_dir+"/" + photo_prefix + "*" + photo_extn
    for f in sorted(glob.glob(globstr),key=photo_sort_key,reverse=True):
        return f
    return None
    
def least_recent_photo():
    # so not rely on string sorting...
    globstr = photo_dir+"/" + photo_prefix + "*" + photo_extn
    for f in sorted(glob.glob(globstr),key=photo_sort_key):
        return f
    return None
                
def current_photo_count():
    globstr = photo_dir+"/" + photo_prefix + "*" + photo_extn
    return len(glob.glob(globstr))
    
def total_photo_count():
    if os.path.exists(last_photo_index_filename):
        last_photo_index = int(open(last_photo_index_filename).read())  
    else:
        last_photo_index = 0
    return last_photo_index

def remove_photo(photo_filename):
    thumbfn = thumb_filename(photo_filename)
    ssdvfn = ssdv_filename(photo_filename)
    for filename in [ photo_filename, thumbfn, ssdvfn ]:
        if os.path.exists(filename):
            try:
                os.unlink(filename)
                print("File %s removed."%(os.path.split(filename)[1],),file=sys.stderr)
            except IOError:
                print("File %s removal failed."%(os.path.split(filename)[1],),file=sys.stderr)
        else:
            print("File %s not found."%(os.path.split(filename)[1],),file=sys.stderr)
    return
