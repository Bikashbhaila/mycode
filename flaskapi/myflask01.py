#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/username")
def hello_world():
   return "This is supposed to be html"

@app.route("/")
def index():
   return "This is the main page"

if __name__ == "__main__":
   app.run(host="localhost", port=3000) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
