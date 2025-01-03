
import urllib.request
import urllib.parse
import traceback

from params import get_param

from tweet_status import make_text_status, make_photo_status

# from https://pymotw.com/3/urllib.request/
import multipartform

def send_text_tweet(twitter,message=None):
    if not message:
        message = make_text_status()
    try:
        url = 'http://%s:%d/tweet'%twitter
        site = get_param("TWEETTARGET","twitter")
        data = urllib.parse.urlencode({'msg': message, 'site': site}).encode()
        response = urllib.request.urlopen(url,data=data).read()
        # check response    
        return message
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(twitter,photo_file,message=None):
    if not message:
        message = make_photo_status(photo_file)
    site = get_param("TWEETTARGET","twitter")
    try:
        # use old fashioned post upload format...
        form = multipartform.MultiPartForm()
        form.add_field('msg', message)
        form.add_field('site', site)
        form.add_file('photo',photo_file,open(photo_file,'rb'))
        data = bytes(form)
        
        url = 'http://%s:%d/tweet'%twitter
        req = urllib.request.Request(url, data=data)
        req.add_header('Content-type', form.get_content_type())
        req.add_header('Content-length', len(data))
        
        response = urllib.request.urlopen(req).read()
        # check response    
        return message
    except:
        traceback.print_exc()
    return False
