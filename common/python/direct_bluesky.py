
from blueskycred import *
from atproto import Client, models

def get_twitter():
    client = Client()
    client.login(username, password)
    return client
