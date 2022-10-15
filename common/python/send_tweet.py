
import sys, traceback, json

from twython import TwythonError as TwitterError

def send_text_tweet(twitter,message):
    try:
        repsonse = twitter.update_status(status=message)
        return True
    except TwitterError:
        traceback.print_exc()
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(twitter,message,photo_file):
    try:
        if isinstance(photo_file,str):
            photo = open(photo_file, 'rb')
        else:
            photo = photo_file
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