
import os, os.path

paramsfile = "/home/pi/.params.sh"

def get_params():
    params = {}
    if os.path.exists(paramsfile):
        for l in open(paramsfile):
            k,v = map(lambda s: s.strip().strip(" '\""),l.split('='))
            params[k] = v
    return params

def get_param(key,default=None):
    return get_params().get(key,default)
    
def get_creds(key,*values,**kwargs):
    default = kwargs.get('default')
    cred = get_param(key,default)
    assert cred is not None
    module = __import__(key.lower()+"-"+cred, globals(), locals(), ['*'], 0)
    return [ getattr(module,v) for v in values ]
