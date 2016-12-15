#! /usr/bin/env python
import datetime

from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/')
def hello_world():
    return """
    <h1>Hello OpenShift</h1>

    """ 

@app.route('/static/<path:path>')
def static_files(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    
