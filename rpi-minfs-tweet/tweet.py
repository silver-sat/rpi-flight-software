
import sys

import find_common_modules

from photo_files import most_recent_photo, remove_photo
from tweet_status import make_text_status, make_photo_status
from minifs_tweet import get_twitter
from minifs_send_tweet import send_text_tweet, send_photo_tweet

filename = most_recent_photo()
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
