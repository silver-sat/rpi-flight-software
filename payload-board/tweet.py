
import sys

import find_common_modules

from tweet_select import tweet_select

from params import get_params

params = get_params()
mode = params.get('TWEETMODE','proxy')
target = params.get('TWEETTARGET','twitter')
text = (params.get('TWEETTEXT','IFNOPHOTO').upper() != 'IFNOPHOTO')

twitter, send_text_tweet, send_photo_tweet = tweet_select(mode, target)
    
from photo_files import least_recent_photo, remove_photo

filename = least_recent_photo()
if not filename or text:
    message = send_text_tweet(twitter)
    if message:
        print("Success! Text Tweet(%s:%s): %s"%(mode,target,message), file=sys.stderr)
else:
    message = send_photo_tweet(twitter, filename)
    if message:
        print("Success! Photo Tweet(%s:%s): %s"%(mode,target,message), file=sys.stderr)
        remove_photo(filename)
