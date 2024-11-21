
from blueskycred import *
from bluesky import BlueSky

def get_twitter():
    client = BlueSky()
    client.login(username, password)
    return client
