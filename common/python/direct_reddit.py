

from params import get_creds
import praw

creds = get_creds("REDDITCRED")

def get_twitter():
    return praw.Reddit(
                client_id=creds.client_id,
                client_secret=creds.client_secret,
                password=creds.password,
                user_agent="silversat payload poster v1.0 by u/silversatorg",
                username=creds.username
            )
