import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lovebox.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ohjhxcerwtorps:9998f1e89262ad9f074318cad1684c52f5b2be35c23204728d3bfa303a18309c@ec2-3-228-235-79.compute-1.amazonaws.com:5432/daiosbhkmkco7u'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'c4bf4de01682284bd683366b'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'login'
loginManager.login_message_category = 'info'

from market import routes
from market import models