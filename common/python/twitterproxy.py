
# import logging
# from http.client import HTTPConnection  # py3

# Log requests made by Twython to twitter
# log = logging.getLogger('urllib3')
# log.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# log.addHandler(ch)
# HTTPConnection.debuglevel = 1

import requests
from twython import Twython

class Twitter(Twython):
    def __init__(self,*args,**kwargs):
        self.httpsproxy = None
        if kwargs.get('httpsproxy'):
            self.httpsproxy = kwargs.get('httpsproxy')
            del kwargs['httpsproxy']
        Twython.__init__(self,*args,**kwargs)
        if self.httpsproxy:
            self.client.get = self.myget
            self.client.post = self.mypost
    def monkeypatch(self,method,url,**kwargs):
        if 'files' in kwargs:
            del kwargs['files']
        req = self.client.prepare_request(
            requests.Request(method=method,
                             url=url,
                             auth=self.client.auth,
                             headers=self.client.headers,
                             **kwargs))
        targethost = url.split('/',3)[2]
        headers = {'Host': targethost}
        headers.update(self.client.headers)
        headers.update({'Authorization': req.headers['Authorization']})
        if targethost in self.httpsproxy:
            url = 'http://' + self.httpsproxy[targethost] + '/' + url.split('/',3)[-1]  
        return url,headers
    def myget(self,url,**kwargs):
        url,headers = self.monkeypatch('get',url,**kwargs)
        return requests.get(url,headers=headers,**kwargs)
    def mypost(self,url,**kwargs):
        url,headers = self.monkeypatch('post',url,**kwargs)
        return requests.post(url,headers=headers,**kwargs)
