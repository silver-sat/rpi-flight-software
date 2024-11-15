
import sys

import find_common_modules

#
# Choose the direct or proxy tweet module depending on whether 
# the ground station rpi is running the ssltunnel daemon to
# turn HTTP twitter API use into HTTPS.
#
# from direct_bluesky import get_twitter
# from direct_reddit import get_twitter
# from direct_tweet import get_twitter
from proxy_tweet import get_twitter

from photo_files import least_recent_photo, remove_photo
# from send_bluesky_tweet import send_text_tweet, send_photo_tweet
# from send_reddit_tweet import send_text_tweet, send_photo_tweet
from send_tweet import send_text_tweet, send_photo_tweet

filename = least_recent_photo()
twitter = get_twitter()
if not filename:
    message = send_text_tweet(twitter)
    if message:
        print("Success! Text Tweet:", message, file=sys.stderr)
else:
    message = send_photo_tweet(twitter, filename)
    if message:
        print("Success! Photo Tweet:", message, file=sys.stderr)
        remove_photo(filename)
