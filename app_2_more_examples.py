# If you want to try this, the easiest way is to temporarily change
# the name of app.py to app-save.py, and change this to app.py

# You could also take the routes from this example and include them in
# the other version, that demonstrates turbo-python
import re
from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route("/hello/<name>")
@app.route("/hello")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )