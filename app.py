#! /usr/bin/env python
import datetime

from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return """
    <h1>Hello Hong</h1>

    <p>From Sam at %(now)s.</p>

    <p>Deployed on Openshift at <a href="%(url)s">%(url)s</a>.</p>
    
    <h2>Serving static Files</h2>
    <ul>
    <li><a href="/static/2014-dragons.html">Static Dragons</a> from <a href="http://js1k.com/">js1k</a>
    </ul>
    """ % dict(
        now=datetime.datetime.now(),
        url="http://cc4-project1-python2-cc4-project1.44fs.preview.openshiftapps.com",
        )

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
