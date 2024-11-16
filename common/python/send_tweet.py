
import sys, traceback, json, time

from tweet_status import make_text_status, make_photo_status

from twython import TwythonError as TwitterError

def update_status(twitter,**params):
    return twitter.post('https://api.twitter.com/2/tweets', params=params, version='2',json_encoded=True)

def send_text_tweet(twitter,message=None):
    if not message:
        message = make_text_status()
    try:
        repsonse = update_status(twitter,text=message)
        return message
    except TwitterError:
        traceback.print_exc()
    except:
        traceback.print_exc()
    return None
    
def send_photo_tweet(twitter,photo_file,message=None):
    try:
        photo = open(photo_file, 'rb')
        start = time.time()
        response = twitter.upload_media(media=photo)
        upload_time = int(round(time.time()-start)) #seconds
        photo.close()
        if 'media_id' not in response:
            print("Twitter upload_media reponse missing media_id:\n"+json.dumps(response,indent=2),file=sys.stderr)
            return None
        else:
            if not message:
                message = make_photo_status(photo_file,upload_time=upload_time)
            repsonse = update_status(twitter, text=message, media=dict(media_ids=[str(response['media_id'])]))
            return message
    except TwitterError:
        traceback.print_exc()
    except:
        traceback.print_exc()
    return None
