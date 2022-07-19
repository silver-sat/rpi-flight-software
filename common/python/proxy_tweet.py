
from twittercred import *
from twitterproxy import Twitter

def get_twitter():
    return Twitter(
               consumer_key,
               consumer_secret,
               access_token,
               access_token_secret,
               httpsproxy={'api.twitter.com': '192.168.100.101:8383',
                           'upload.twitter.com': '192.168.100.101:8484'}
           )
