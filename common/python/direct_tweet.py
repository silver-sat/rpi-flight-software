
from params import get_creds
from twython import Twython as Twitter

consumer_key,consumer_secret,access_token,access_token_secret = \
    get_creds("TWITTERCRED","consumer_key","consumer_secret","access_token","access_token_secret")

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
           )