
from params import get_creds
import praw, sys

def get_twitter():
    creds = get_creds("REDDITCRED")
    print("u/"+creds.username,file=sys.stderr)
    return praw.Reddit(
                client_id=creds.client_id,
                client_secret=creds.client_secret,
                password=creds.password,
                user_agent="silversat payload poster v1.0 by u/silversatorg",
                username=creds.username
            )
