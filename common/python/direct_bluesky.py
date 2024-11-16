
from blueskycred import *
from atproto_client.client.client import Client

def get_twitter():
    client = Client()
    client.login(username, password)
    return client
