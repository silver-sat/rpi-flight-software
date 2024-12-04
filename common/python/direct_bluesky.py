
from params import get_creds
from bluesky import BlueSky

def get_twitter():
    creds = get_creds("BLUESKYCRED")
    client = BlueSky()
    client.login(creds.username, creds.password)
    return client
