#USAGE: getRandomFileBytes("./static/images/")
import os
from random import randint as rand

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
from flask import make_response

def getRandomFilepath(folder: str):
    files = os.listdir(folder)
    return folder + files[rand(0, len(files)-1)]

def getRandomFileBytes(path: str):
    return open(getRandomFilepath(path), "r+b").read()



app = Flask(__name__)
app.wsgi_app = ProxyFix(
   app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def index():
   response = make_response(getRandomFileBytes("./static/"))
   response.headers.set("Content-Type","image/png")
   return response