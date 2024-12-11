
import datetime, os, os.path, shutil

from photo_files import current_photo_count, total_photo_count, 
                           photo_sort_key, least_recent_photo

textstatusfile = "/home/pi/.textstatus.txt"
textstatusdefault = "[%(now)s] Twitter text status!"
photostatusfile = "/home/pi/.photostatus.txt"
photostatusdefault = "[%(now)s] Twitter photo status! Photo: %(filename)s, Size: %(size)d"

def timestamp(msg):
    return "[%s] %s"%(datetime.datetime.now().ctime(),msg)

def getdata(photo_filename=None, **kwargs):
    diskfree = "%.2f"%(shutil.disk_usage(os.path.expanduser("~")).free/(1024**3),)
    if photo_filename:
        size = os.path.getsize(photo_filename)
        fname = os.path.split(photo_filename)[1]
        current_photo=photo_sort_key(fname)
    else:
        size = -1
        fname = ""
        current_photo = photo_sort_key(least_recent_photo())
    return dict(now=datetime.datetime.now().ctime(),
                filename=fname,size=size,
                photos_on_disk=current_photo_count(),
                total_photos=total_photo_count(),
                sent_photos=(total_photos-photos_on_disk),
                current_photo = current_photo,
                upload_time=kwargs.get("upload_time",-1),
                disk_free=diskfree)

def getfmtstr(filename,fmtstr):
    if os.path.exists(filename):
        return open(filename).read().strip()
    return fmtstr
            
def make_text_status(**kwargs):
    fmtstr = getfmtstr(textstatusfile,textstatusdefault)
    data = getdata(**kwargs)
    return fmtstr%data
		
def make_photo_status(photo_filename, **kwargs):
    fmtstr = getfmtstr(photostatusfile,photostatusdefault)
    data = getdata(photo_filename=photo_filename, **kwargs)
    return fmtstr%data

