#!/bin/env python3

# importing the required libraries
import os, os.path, sys, glob, time, datetime
from hashlib import md5
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from waitress import serve
import socket
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# initialising the flask app
app = Flask("minifs")

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
upload_photo_folder = "uploads/photos"
if not os.path.exists(upload_photo_folder):
    os.makedirs(upload_photo_folder)
app.config['UPLOAD_FOLDER'] = "uploads"
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route('/upload', methods = ['POST'])
def upload():
   if request.method == 'POST': # check if the method is post
      f = request.files['file'] # get the file from the files object
      if f.filename == "" or secure_filename(f.filename) == "":
          return "Bad filename\n",400
      # All files are cleaned up, we retain the filename
      # All files are placed in a time-stamped folder
      sfilename = os.path.split(secure_filename(f.filename))[1]
      dtfolder = time.strftime("%Y%m%d-%H%M%S")
      if not os.path.exists(os.path.join("uploads",dtfolder)):
          try:
              lastfolder = sorted([ f for f in os.listdir("uploads") if f != "photos" ])[-1]
          except IndexError:
              lastfolder = None
          if lastfolder:
              t0 = datetime.datetime.strptime(lastfolder,"%Y%m%d-%H%M%S")
              t1 = datetime.datetime.strptime(dtfolder,"%Y%m%d-%H%M%S")
              if (t1-t0) < datetime.timedelta(minutes=5):
                  dtfolder = lastfolder
              else:
                  os.makedirs(os.path.join("uploads",dtfolder))
          else:
              os.makedirs(os.path.join("uploads",dtfolder))
      i = 0; extra = ""
      while os.path.exists(os.path.join("uploads",dtfolder,secure_filename(sfilename))+extra):
          i += 1
          extra = '-' + str(i)
      thefilename = secure_filename(sfilename)+extra
      f.save(os.path.join("uploads",dtfolder,thefilename)) 
      return 'Success\n', 200 # Display this message after uploading
   return 'Bad method\n', 400

@app.route('/download')
def download():
    filename = os.path.join('downloads',request.args['file'])
    if os.path.exists(filename):
        return send_file(os.path.join('downloads',request.args['file']), as_attachment=True)
    return "No such file\n", 400

@app.route('/list')
def list():
    pattern = request.args.get('pattern','*')
    filelist = []
    for f in glob.glob('downloads/'+pattern):
        filename = f.split('/',1)[1]
        size = str(os.path.getsize(f))
        md5hash = md5(open(f).read()).hexdigest().lower()
        filelist.append("\t".join([filename,size,md5hash]))
    filelist.sort()
    return "\n".join(filelist)+'\n'


import http.client

HOP_BY_HOP_HEADERS = {
    'connection',
    'keep-alive',
    'proxy-authenticate',
    'proxy-authorization',
    'te',
    'trailers',
    'transfer-encoding',
    'upgrade',
    'expect'
}

@app.route('/<path:path>', methods=['POST'])
def tweet_proxy(path):
    try:
        conn = http.client.HTTPConnection("127.0.0.1", 8485)
        conn.putrequest("POST", f"/{path}", skip_host=True)

        # Rebuild headers, filtering out hop-by-hop and setting Host
        for key, value in request.headers.items():
            if key.lower() not in HOP_BY_HOP_HEADERS and key.lower() != 'host':
                conn.putheader(key, value)
        conn.putheader("Host", "upload.twitter.com")         # Adds correct Host manually
        conn.endheaders()

        # Send raw body
        body = request.get_data()
        logging.info(f"Sending to: /{path}") 
        for k, v in request.headers.items(): 
           logger.info(f"Header: {k}: {v}")
        logging.info(f"Body length: {len(body)}")
        conn.send(body)

        # Get response
        resp = conn.getresponse()
        data = resp.read()
        headers = [(k, v) for (k, v) in resp.getheaders() if k.lower() not in HOP_BY_HOP_HEADERS]
        return (data, resp.status, headers)

    except Exception as e:
        return f"Proxy error: {e}", 500


if __name__ == '__main__':
   # app.run(host='127.0.0.1',port=5001) # running the flask app
   # app.run(host=sys.argv[1],port=5001) # running the flask app
   orig_socket = socket.socket 
   def patched_socket(*args, **kwargs): 
      s = orig_socket(*args, **kwargs) 
      s.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 512) 
      return s 
   socket.socket = patched_socket 
   # added to handle two app.py instances
   port = int(sys.argv[2]) if len(sys.argv) > 2 else 5001
   serve(app, host=sys.argv[1], port=port) 
   # serve(app, host=sys.argv[1], port=5001)

