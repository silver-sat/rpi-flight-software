
import sys, traceback, json

from twittercred import *
from Twython import Twython as Twitter
from Twython import TwythonError as TwitterError

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
           )

def send_text_tweet(message):
    try:
        twitter = get_twitter()
        repsonse = twitter.update_status(status=message)
        return True
    except TwitterError:
        traceback.print_exc()
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(message,photo_filename):
    try:
        twitter = get_twitter()
        photo = open(photo_filename, 'rb')
        response = twitter.upload_media(media=photo)
        photo.close()
        if 'media_id' not in response:
            print("Twitter upload_media reponse missing media_id:\n"+json.dumps(response,indent=2),file=sys.stderr)
            return False
        else:
            repsonse = twitter.update_status(status=message, media_ids=[response['media_id']])
            return True
    except TwitterError:
        traceback.print_exc()
    except:
        traceback.print_exc()
    return False