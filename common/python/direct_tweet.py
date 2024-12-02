
from params import get_creds
from twython import Twython as Twitter

creds = get_creds("TWITTERCRED")

def get_twitter():
    return Twitter(
               creds.consumer_key,
               creds.consumer_secret,
               creds.access_token,
               creds.access_token_secret,
           )
