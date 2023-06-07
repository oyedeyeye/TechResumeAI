#!/usr/bin/python3
""" Flask Application script"""
from flask import Flask
from models.engine.db_storage import db, DBStorage
from models.user import User
from models.resume_info import Resume_info
from models.template import Template


"""create the app"""
app = Flask(__name__)
app.url_map.strict_slashes = False
db_storage = DBStorage()
db_storage.setup_db(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
