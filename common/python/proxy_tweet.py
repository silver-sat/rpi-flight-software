
from twittercred import *
from twitterproxy import Twitter

from params import get_param

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
