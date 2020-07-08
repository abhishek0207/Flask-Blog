from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '93f1182d275f5c3c1c668866e791efa9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #relative path from current file
db = SQLAlchemy(app) #DB instance db strucuture is proposed as classes or models
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #function name of the route
login_manager.login_message_category = 'info'
from flaskblog import routes