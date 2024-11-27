

from params import get_creds
import praw

username,password,client_id,client_secret = \
     get_creds("REDDITCRED","username","password","client_id","client_secret")

def get_twitter():
    return praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                password=password,
                user_agent="silversat payload poster v1.0 by u/silversatorg",
                username=username
            )
