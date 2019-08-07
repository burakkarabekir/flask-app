__author__ = 'burakk'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '5bae0a0a9e5c83ba168abdc34f5872cd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///you.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

