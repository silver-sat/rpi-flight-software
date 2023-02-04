
import sys, traceback, json

subreddit_name = "test" #change later

def send_text_tweet(reddit,message):
    try:
        reddit.subreddit(subreddit_name).submit(title=message, selftext='')
        return True
    except:
        traceback.print_exc()
    return False
    
def send_photo_tweet(reddit,message,photo_file):
    # photo_file must be on the file system
    try:
        reddit.subreddit(subreddit_name).submit_image(title=message, image_path=photo_file, without_websockets = True)
        return True
    except:
        traceback.print_exc()
    return False
