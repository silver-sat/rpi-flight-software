
from params import get_param, get_creds
from bluesky import BlueSky

username,password = get_creds("BLUESKYCRED","username","password")

def get_twitter():
    client = BlueSky(base_url="http://%s:8585/"%(get_param('GROUND_IP'),))
    client.login(username, password)
    return client
