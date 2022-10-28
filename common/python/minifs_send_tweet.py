
import urllib.request
import urllib.parse
import traceback
import multipartform

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
        # use old fashioned post upload format...
        form = multipartform.MultiPartForm()
        form.add_field('msg', message)
        form.add_file('photo',photo_file,open(photo_file,'rb'))
        data = bytes(form)
        
        url = 'http://%s:%d/tweet'%twitter
        req = urllib.request.Request(url, data=data)
        req.add_header('Content-type', form.get_content_type())
        req.add_header('Content-length', len(data))
        
        response = urllib.request.urlopen(req).read()
        # check response    
        return True
    except:
        traceback.print_exc()
    return False
