
import sys, urllib.request, urllib.parse, json, datetime

class BlueSkyError(RuntimeError):
    """ Exception for BlueSky errors """

class BlueSkyLoginError(BlueSkyError):
    def __init__(self,*args,**kwargs):
        super().__init__("Login failed",*args,**kwargs)

class BlueSkyRefreshError(BlueSkyError):
    def __init__(self,*args,**kwargs):
        super().__init__("Session refresh failed",*args,**kwargs)

class BlueSkyAPIError(BlueSkyError):
    def __init__(self,request,*args,**kwargs):
        super().__init__("%s api call Session refresh failed"%(request,),*args,**kwargs)

class BlueSky(object):
    def __init__(self,**kwargs):
        self.url=kwargs.get('base_url','https://bsky.social/')

    def login(self,user,password):
        payload = {"identifier": user, "password": password}
        self.user = user
        self.password = password
        result = self.jsonwspostreq('xrpc/com.atproto.server.createSession',payload)
        if 'accessJwt' not in result:
            raise BlueSkyLoginError()
        self.accessJwt = result['accessJwt']
        self.refreshJwt = result['refreshJwt']
        

    def refresh_session(self):
        headers={"Authorization": "Bearer "+self.refreshJwt} 
        result = self.jsonwspostreq('xrpc/com.atproto.server.refreshSession',headers=headers)
        if 'accessJwt' not in result:
            raise BlueSkyRefreshError()
        self.accessJwt= result['accessJwt']
        self.refreshJwt = result['refreshJwt']

    def timestamp(self):
        return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds').split('+')[0]+"Z"

    def send_post(self,msg,**kwargs):
        self.refresh_session()
        headers={"Authorization": "Bearer "+self.accessJwt} 
        payload={"repo": self.user, "collection": "app.bsky.feed.post", 
                 "record": {"text": msg, "createdAt": self.timestamp()}}
        payload["record"].update(kwargs)
        result = self.jsonwspostreq('xrpc/com.atproto.repo.createRecord',payload=payload,headers=headers)
        if 'cid' not in result:
            raise BlueSkyAPIError("createRecord")
        return result

    def upload_blob(self,data):
        self.refresh_session()
        headers={"Authorization": "Bearer "+self.accessJwt} 
        result = self.jsonwspostreq('xrpc/com.atproto.repo.uploadBlob',payload=data,headers=headers)
        if 'blob' not in result:
            raise BlueSkyAPIError("uploadBlob")
        return result

    def jsonwspostreq(self,request,payload={},headers={}):
        return self.jsonwsreq(request,payload,'POST',headers)

    def jsonwsreq(self,request,payload={},method='GET',headers={}):
        theheaders = {'Content-type': 'application/json',
                      'Accept':       'application/json'}
        theheaders.update(headers)
        opener = urllib.request.build_opener(urllib.request.HTTPHandler())                                 
        url = self.url + request
        if method == 'GET':
            if payload != {}:
                url += '?' + urllib.parse.urlencode(payload)
            request = urllib.request.Request(url, headers=theheaders)
        elif method == 'POST':
            if payload != {}:
                if isinstance(payload,bytes):
                    # theheaders['Content-length'] = str(len(payload))
                    theheaders['Content-type'] = 'application/octet-stream'
                    request = urllib.request.Request(url, payload, headers=theheaders)
                else:
                    request = urllib.request.Request(url, json.dumps(payload).encode(), headers=theheaders)
            else:
                request = urllib.request.Request(url, "".encode(), headers=theheaders) 
        else:
            raise ValueError('Bad method '+method)
        # print(url,payload,theheaders)
        try:
            return json.loads(opener.open(request).read())
        except urllib.request.HTTPError as e:
            return {u'error': True, u'errorcode': e.code, u'errormsg': e.msg} 
        return {u'error': True}      

if __name__ == '__main__':
    
    bsky = BlueSky()
    bsky.login('edwardsnj.bsky.social', 'XXXXXXXXXXXXXXX')
    if len(sys.argv) <= 2:
        bsky.send_post(sys.argv[1])
    else:
        data = open(sys.argv[2],'rb').read()
        blob = bsky.upload_blob(data)
        embed = { "$type": "app.bsky.embed.images", "images": [ { "alt": "", "image": blob['blob'] } ] }
        bsky.send_post(sys.argv[1],embed=embed)
