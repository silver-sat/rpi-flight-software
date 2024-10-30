
import datetime, os, os.path

from photo_files import current_photo_count, total_photo_count, photo_sort_key

textstatusfile = "/home/pi/.textstatus"
textstatusdefault = "[%(now)s] Twitter text status!"
photostatusfile = "/home/pi/.photostatus"
photostatusdefault = "[%(now)s] Twitter photo status! Photo: %(filename)s, Size: %(size)d"

def timestamp(msg):
    return "[%s] %s"%(datetime.datetime.now().ctime(),msg)

def getdata(photo_filename=None):
    if photo_filename:
        size = os.path.getsize(photo_filename)
        fname = os.path.split(photo_filename)[1]
    else:
        size = -1
        fname = ""
    return dict(now=datetime.datetime.now().ctime(),
                filename=fname,size=size,
                photos_on_disk=current_photo_count(),
                total_photos=total_photo_count(),
                current_photo=photo_sort_key(fname))

def getfmtstr(filename,fmtstr):
    if os.path.exists(filename):
        return open(filename).read().strip()
    return fmtstr
            
def make_text_status():
    fmtstr = getfmtstr(textstatusfile,textstatusdefault)
    data = getdata()
    return fmtstr%data
		
def make_photo_status(photo_filename):
    fmtstr = getfmtstr(photostatusfile,photostatusdefault)
    data = getdata(photo_filename)
    return fmtstr%data

