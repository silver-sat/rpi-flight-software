
import sys, traceback, json, time

from tweet_status import make_text_status, make_photo_status

def send_text_tweet(bluesky,message=None):
    if not message:
        message = make_text_status()
    try:
        repsonse = bluesky.send_post(message)
        return message
    except:
        traceback.print_exc()
    return None
    
def send_photo_tweet(bluesky,photo_file,message=None):
    try:
        photo = open(photo_file, 'rb').read()
        start = time.time()
        image = bluesky.upload_blob(photo)
        upload_time = int(round(time.time()-start)) #seconds
        photo.close()
        if not message:
            message = make_photo_status(photo_file,upload_time=upload_time)
        embed = embed = { "$type": "app.bsky.embed.images", "images": [ { "alt": "", "image": image['blob'] } ] }
        repsonse = bluesky.send_post(message, embed=embed)
        return message
    except:
        traceback.print_exc()
    return None
