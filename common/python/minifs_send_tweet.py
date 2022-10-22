
import urllib.request
import urllib.parse
import traceback

def send_text_tweet(twitter,message):
    try:
        url = 'http://%s:%d/tweet'%twitter
        data = urllib.parse.urlencode({'msg': message}).encode()
        response = urllib.request.urlopen(url,data=data).read()
        # check response    
        return True
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(twitter,message,photo_file):
    try:
        if isinstance(photo_file,str):
            photodata = open(photo_file, 'rb').read()
        else:
            photodata = photo_file.read()
        url = 'http://%s:%d/tweet'%twitter
        data = urllib.parse.urlencode({'msg': message, 'photo': photodata}).encode()
        # this does not work!
        response = urllib.request.urlopen(url,data=data).read()
        # check response    
        return True
    except:
        traceback.print_exc()
    return False
