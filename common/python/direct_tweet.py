
from params import get_creds
from twython import Twython as Twitter

def get_twitter():
    creds = get_creds("TWITTERCRED")
    return Twitter(
               creds.consumer_key,
               creds.consumer_secret,
               creds.access_token,
               creds.access_token_secret,
           )
