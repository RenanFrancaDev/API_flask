from flask import request, jsonify, Flask
import random as rk
import os
import threading
from .static import spreadsheet


app = Flask(__name__)
port = "5000"

# Open a ngrok tunnel to the HTTP server
public_url = ngrok.connect(port).public_url
print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")

# Update any base URLs to use the public ngrok URL
app.config["BASE_URL"] = public_url

@app.route("/") #code to assign HomePage URL in our app to function home.

def home():
  '''
  The entire line below must be written in a single line.
  '''
  return "<marquee><h2> TO CHECK THIS APP OUTPUT USE THE ROUTE '/index'.</h2></marquee>"

@app.route("/index") #return JSON object

def input():
  return jsonify(spreadsheet)

 # Start the Flask server in a new thread
threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
