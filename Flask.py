#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

app.debug = True


@app.route('/')
def index():
    return 'hello word'


if __name__ == '__main__':
    app.run()
