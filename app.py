# This version demonstrates the use of turbo_flask.
# Things to note:
# 1. Note the call to "threading.Thread(target=update_load).start()"
#    To understand this, you will have to read about python threading module.
#    Basically this starts a new process that keeps calling the update_load 
#    function.
# 2.  Note the convenience of using templates and how they can be componentized.
#     For instance, the index.html template includes the base.html template by 
#     stating: {% extends "base.html" %}.  This will be usefull in creating pieces
#     of html that can be used in multiple locations.
#     
#    

import random
import re
import sys
from flask import Flask, render_template

import threading
import time
from turbo_flask import Turbo


app = Flask(__name__)
turbo = Turbo(app)

# ...

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(5)
            turbo.push(turbo.replace(render_template('loadavg.html'), 'load'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/ui-mockup')
def uimockup():
    return render_template('ui-mockup.html')

@app.context_processor
def inject_load():
    if sys.platform.startswith('linux'): 
        with open('/proc/loadavg', 'rt') as f:
            load = f.read().split()[0:3]
    else:
        load = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'load1': load[0], 'load5': load[1], 'load15': load[2]}

if __name__ == '__main__':
# Use this if you are testing locally on a computer and are not conneting via the network.
#    app.run(host='0.0.0.0', threaded=True)
# use a line like this if you want to access your flask app remotely from the same network.
# if so, set the address to the address that you ssh to, and make sure both the pi and remore computer
# are on the same wireless network.
    app.run(host='192.168.1.116',   threaded=True)

