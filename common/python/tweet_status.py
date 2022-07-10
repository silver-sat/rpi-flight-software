
import datetime

def timestamp(msg):
    return "[%s] %s"%(datetime.datetime.now().ctime(),msg)

def make_text_status():
    return timestamp("Twitter text status!")
		
def make_photo_status(photo_filename):
    size = os.path.getsize(photo_filename)
    fname = os.path.split(photo_filename)[1]
    return timestamp("Twitter photo status! Photo: %s, Size: %d"%(fname,size))

