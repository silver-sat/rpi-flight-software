
from params import get_param, get_creds
from twitterproxy import Twitter

creds = get_creds("TWITTERCRED")

def get_twitter():
    groundip = get_param('GROUND_IP')
    return Twitter(
               creds.consumer_key,
               creds.consumer_secret,
               creds.access_token,
               creds.access_token_secret,
               httpsproxy={'api.twitter.com': groundip + ':8383',
                           'upload.twitter.com': groundip + ':8484'}
           )
