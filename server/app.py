#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# append to server/app.py

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'
