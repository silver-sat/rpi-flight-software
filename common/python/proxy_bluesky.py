
from params import get_param, get_creds
from bluesky import BlueSky

def get_twitter():
    creds = get_creds("BLUESKYCRED")
    client = BlueSky(base_url="http://%s:8585/"%(get_param('GROUND_IP'),))
    client.login(creds.username, creds.password)
    return client
