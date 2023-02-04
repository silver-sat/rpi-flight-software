
from redditcred import *
import praw

def get_twitter():
    return praw.Reddit(
                client_id=client_id,
                client_secret=client_secret,
                password=password,
                user_agent="silversat payload poster v1.0 by u/silversatpayloaddevs",
                username=username
            )
