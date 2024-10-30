
import sys

import find_common_modules

#
# Choose the direct or proxy tweet module depending on whether 
# the ground station rpi is running the ssltunnel daemon to
# turn HTTP twitter API use into HTTPS.
#
# from direct_tweet import get_twitter
from proxy_tweet import get_twitter

from photo_files import least_recent_photo, remove_photo
from tweet_status import make_text_status, make_photo_status
from send_tweet import send_text_tweet, send_photo_tweet

filename = least_recent_photo()
twitter = get_twitter()
if not filename:
    message = make_text_status()
    if send_text_tweet(twitter,message):
        print("Success! Text Tweet:",message,file=sys.stderr)
else:
    message = make_photo_status(filename)
    if send_photo_tweet(twitter,message, filename):
        print("Success! Photo Tweet:",message,file=sys.stderr)
        remove_photo(filename)
