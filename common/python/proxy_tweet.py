
from params import get_param, get_creds
from twitterproxy import Twitter

consumer_key,consumer_secret,access_token,access_token_secret = \
    get_creds("TWITTERCRED","consumer_key","consumer_secret","access_token","access_token_secret")

def get_twitter():
    groundip = get_param('GROUND_IP')
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
               httpsproxy={'api.twitter.com': groundip + ':8383',
                           'upload.twitter.com': groundip + ':8484'}
           )
