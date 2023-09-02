#!/bin/env python3

# importing the required libraries
import os, os.path, sys, glob, time
from hashlib import md5
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

# initialising the flask app
app = Flask("minifs")

# Creating the upload folder
upload_folder = "uploads/"
if not os.path.exists(upload_folder):
    os.makedirs(upload_folder)
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
      dtfolder = time.strftime("%Y%m%d-%H%M")
      if not os.path.exists(os.path.join("uploads",dtfolder)):
          lastfolder = sorted(os.listdir("uploads"))[-1]
          t0 = datetime.strptime("%Y%m%d-%H%M",lastfolder)
          t1 = datetime.strptime("%Y%m%d-%H%M",dtfolder)
          # print(t0,t1)
          if (t1-t0) > datetime.datetime(sec=600):
              os.makedirs(os.path.join("uploads",dtfolder))
          else:
              dtfolder = lastfolder
      f.save(os.path.join("uploads",dtfolder,secure_filename(sfilename))) # this will secure the file
      return 'Success\n', 200 # Display thsi message after uploading
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

import find_common_modules
from direct_tweet import get_twitter
from send_tweet import send_photo_tweet, send_text_tweet

@app.route('/tweet', methods = ['GET','POST'])
def tweet():
    
    twitter = get_twitter()
    
    message = request.values['msg']
    if 'photo' in request.files:
        f = request.files['photo']
        if f.filename == "" or secure_filename(f.filename) == "":
            return "Bad filename\n",400

        if not send_photo_tweet(twitter,message,f.stream):
            print("something went wrong!")
            return "Bad tweet error?",400
        print("Tweeted: %s with image %s" % (message, f.filename))
            
    else:
        if not send_text_tweet(twitter,message):
            print("something went wrong!")
            return "Bad tweet error?",400   
        print("Tweeted: %s without image" % (message,))
    
    return "Successfull tweet", 200

if __name__ == '__main__':
   # app.run(host='127.0.0.1',port=5001) # running the flask app
   app.run(host=sys.argv[1],port=5001) # running the flask app

 
