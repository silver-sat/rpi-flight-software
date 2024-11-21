
from blueskycred import *
from bluesky import BlueSky

from params import get_param

def get_twitter():
    client = BlueSky(base_url="http://%s:8585/"%(get_param('GROUND_IP'),))
    client.login(username, password)
    return client
