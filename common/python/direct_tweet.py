
from twittercred import *
from twython import Twython as Twitter
from twython import TwythonError as TwitterError

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
           )

from send_tweet import *