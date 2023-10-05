import os
from werkzeug.middleware.proxy_fix import ProxyFix
from flask import Flask
from flask import make_response

app = Flask(__name__)

app.wsgi_app = ProxyFix(
   app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

@app.route("/")
def index():
   response = make_response(open("./static/test.png","r+b").read())
   response.headers.set("Content-Type","image/png")
   return response
