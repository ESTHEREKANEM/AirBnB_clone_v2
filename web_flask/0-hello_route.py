#!/usr/bin/python3
'''A flask web application
'''
from flask import Flask


app = Flask(__name__)
'''My Flask instance'''
@app.route('/', strict_slashes=False)

def hello():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
