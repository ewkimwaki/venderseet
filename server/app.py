#!/usr/bin/env python3
from models import db, Sweet, Vendor, VendorSweet
from flask_migrate import Migrate
from flask import Flask, request, make_response
from flask_restful import Api, Resource
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__,
    static_url_path='',
    static_folder='../client/build',
    template_folder='../client/build')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

from routes import *

if __name__ == '__main__':
    app.run(port=5555, debug=True)
