#!/usr/bin/python3
""" Flask Application script"""
import os
import sys
sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(__file__), '../../')))
from flask import Flask
from models.engine.db_storage import db, DBStorage
from models.user import User
from models.resume_info import Resume_info
from models.template import Template
# Load environment variable
from dotenv import load_dotenv
load_dotenv()

"""create the app"""
app = Flask(__name__)
app.url_map.strict_slashes = False
db_storage = DBStorage(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
