
import sys, traceback, json, time

from tweet_status import make_text_status, make_photo_status

subreddit_name = "sandboxtest" #change later

def status_split(message):
    l = [ s.strip() for s in message.split('\n',1) ]
    if len(l) == 1:
        return l[0],""
    return l[0],l[1]

def send_text_tweet(reddit,message=None):
    if not message:
        message,rest = status_split(make_text_status())
    else:
        message,rest = status_split(message)
    try:
        reddit.subreddit(subreddit_name).submit(title=message, selftext=rest)
        return (message+"\n"+rest).strip()
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(reddit,photo_file,message=None):
    if not message:
        message = make_photo_status(photo_file)
    # photo_file must be on the file system
    try:
        reddit.subreddit(subreddit_name).submit_image(title=message, image_path=photo_file, without_websockets = True)
        return message
    except:
        traceback.print_exc()
    return False
