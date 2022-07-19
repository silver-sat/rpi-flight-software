
from twittercred import *
from twython import Twython as Twitter

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
           )