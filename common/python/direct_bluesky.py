
from params import get_creds
from bluesky import BlueSky

username,password = get_creds("BLUESKYCRED","username","password")

def get_twitter():
    client = BlueSky()
    client.login(username, password)
    return client
