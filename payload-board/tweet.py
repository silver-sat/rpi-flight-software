
import sys

import find_common_modules
from params import get_params

params = get_params()
target = params.get('TWEETTARGET','twitter')
mode = params.get('TWEETMODE','proxy')

import direct_bluesky, direct_reddit, direct_tweet
import proxy_tweet, minifs_tweet

import send_tweet, send_bluesky_tweet, send_reddit_tweet
import send_minifs_tweet

assert mode in ("direct","proxy","minifs")
if mode == "direct":
    assert target in ("twitter","reddit","bluesky")
    if target == "twitter":
        twitter = direct_tweet.get_twitter()
        send_text_tweet = send_tweet.send_text_tweet
        send_photo_tweet = send_tweet.send_photo_tweet
    elif target == "reddit":
        twitter = direct_reddit.get_twitter()
        send_text_tweet = send_reddit_tweet.send_text_tweet
        send_photo_tweet = send_reddit_tweet.send_photo_tweet
    elif target == "bluesky":
        twitter = direct_bluesky.get_twitter()
        send_text_tweet = send_blueskey_tweet.send_text_tweet
        send_photo_tweet = send_blueskey_tweet.send_photo_tweet
elif mode == "proxy":
    assert target in ("twitter",)
    twitter = proxy_twitter.get_twitter()
    send_text_tweet = send_tweet.send_text_tweet
    send_photo_tweet = send_tweet.send_photo_tweet
elif mode == "minifs":
    twitter = minifs_tweet.get_twitter()
    send_text_tweet = send_minifs_tweet.send_text_tweet
    send_photo_tweet = send_minifs_tweet.send_photo_tweet

from photo_files import least_recent_photo, remove_photo

filename = least_recent_photo()
if not filename:
    message = send_text_tweet(twitter)
    if message:
        print("Success! Text Tweet(%s): %s"%(site, message), file=sys.stderr)
else:
    message = send_photo_tweet(twitter, filename)
    if message:
        print("Success! Photo Tweet(%s): %s"%(site, message), file=sys.stderr)
        remove_photo(filename)
