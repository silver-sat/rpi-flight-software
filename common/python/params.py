
def get_params():
    params = {}
    for l in open("/home/pi/.params.sh"):
        k,v = map(lambda s: s.strip().strip(" '\""),l.split('='))
        params[k] = v
    return params

def get_param(key,default=None):
    return get_params().get(key,default)