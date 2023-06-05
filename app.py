#!/usr/bin/python3
""" Flask Application script"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""create the database extension"""
db = SQLAlchemy()

"""create the app"""
app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://<username>:<password>@localhost/<database>'

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)