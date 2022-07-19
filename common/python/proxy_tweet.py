
from twittercred import *
from twitterproxy import Twitter
from twython import TwythonError as TwitterError

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
               httpsproxy={'api.twitter.com': '192.168.100.101:8383',
                           'upload.twitter.com': '192.168.100.101:8484'}
           )

from send_tweet import send_text_tweet, send_photo_tweet