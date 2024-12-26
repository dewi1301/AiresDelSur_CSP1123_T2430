from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Prevent warnings
app.config['SESSION_COOKIE_SECURE'] = True  # Secure cookies for production
app.config['SECRET_KEY'] = '36156d54587397cb17ecf992'

from routes import *
