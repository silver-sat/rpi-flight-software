
from params import get_creds
from bluesky import BlueSky

creds = get_creds("BLUESKYCRED")

def get_twitter():
    client = BlueSky()
    client.login(creds.username, creds.password)
    return client
