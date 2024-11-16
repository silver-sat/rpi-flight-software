#!/bin/env python3

# importing the required libraries
import os, os.path, sys, glob, time, datetime
from hashlib import md5
from flask import Flask, request, send_file
from werkzeug.utils import secure_filename

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
              lastfolder = sorted(os.listdir("uploads"))[-1]
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

import find_common_modules
import direct_tweet, send_tweet
import direct_bluesky, send_bluesky_tweet
import direct_reddit, send_reddit_tweet

@app.route('/tweet', methods = ['GET','POST'])
def tweet():
    sites = [ s.strip() for s in request.values.get('site','twitter').split(",") ]
    for site in sites:
    
        if site == "twitter":
            twitter = direct_tweet.get_twitter()
            send_text_tweet = send_tweet.send_text_tweet
            send_photo_tweet = send_tweet.send_photo_tweet
        elif site == "reddit":
            twitter = direct_reddit.get_twitter()
            send_text_tweet = send_reddit_tweet.send_text_tweet
            send_photo_tweet = send_reddit_tweet.send_photo_tweet
        elif site == "bluesky":
            twitter = direct_bluesky.get_twitter()
            send_text_tweet = send_bluesky_tweet.send_text_tweet
            send_photo_tweet = send_bluesky_tweet.send_photo_tweet
        else:
            continue
       
        message = request.values['msg']
        if 'photo' in request.files:
            f = request.files['photo']
            if f.filename == "" or secure_filename(f.filename) == "":
                return "Bad filename\n",400
            sfilename = os.path.split(secure_filename(f.filename))[1]
            photo_file = os.path.join(upload_photo_folder,sfilename)
            f.save(photo_file)

            if not send_photo_tweet(twitter,photo_file,message):
                print("something went wrong!")
                return "Bad tweet error?",400
            print("Tweeted(%s): %s with image %s" % (site,message, f.filename))
            os.path.unlink(photo_file)
        else:
            if not send_text_tweet(twitter,message):
                print("something went wrong!")
                return "Bad tweet error?",400   
            print("Tweeted(%s): %s without image" % (site,message,))
    
    return "Successfull tweet", 200

if __name__ == '__main__':
   # app.run(host='127.0.0.1',port=5001) # running the flask app
   app.run(host=sys.argv[1],port=5001) # running the flask app

 
