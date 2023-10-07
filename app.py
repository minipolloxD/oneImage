#USAGE: getRandomFileBytes("./static/images/")
import os
import dataclasses
from random import randint as rand

from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
from flask import make_response

def getRandomFilepath(folder: str):
    files = os.listdir(folder)
    return folder + files[rand(0, len(files)-1)]

class fileMeta:
    filename : str = ""
    extension : str = ""
    bytes : bytes = None

    def getMIME(self):
        match self.extension:
            case "png":
                return "image/png"
            case "jpg":
                return "image/jpeg"
            case "jpeg":
                return "image/jpeg"
            case "gif":
                return "image/gif"
            case "webm":
                return "video/webm"

    def __init__(self, filepath : str):
        self.filename = filepath.split("/")[-1]
        self.extension = filepath.split(".")[-1]
        self.bytes = open(filepath, "r+b").read()

def getRandomFile() -> fileMeta:
    return fileMeta(getRandomFilepath)

app = Flask(__name__)
app.wsgi_app = ProxyFix(
   app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def index():
   file = getRandomFile()
   
   response = make_response(file.bytes)
   response.headers.set("Content-Type", file.getMIME())
   
   return response