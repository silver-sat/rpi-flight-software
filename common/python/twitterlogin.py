
from twittercred import *
from twython import Twython as Twitter

import sys

twitter = Twitter(
               consumer_key,
               consumer_secret
           )

auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

print("Login at URL:",auth['auth_url'],file=sys.stderr)

print("Look at SilverSat homepage url and copy and paste oauth_verifier value: ",end="",file=sys.stderr)
oauth_verifier = input().strip()

twitter = Twitter(consumer_key, consumer_secret,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)

OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']


print("Here is the new twittercred.py:",file=sys.stderr)
print(("""
# Known as API key on twitter website
consumer_key    	= '%s'
# Known as API secret key on twitter website
consumer_secret 	= '%s'
access_token    	= '%s'
access_token_secret = '%s'
"""%(consumer_key, consumer_secret, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)).strip())
