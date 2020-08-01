from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

from flaskblog.config import Config


# app.config['SECRET_KEY'] = '93f1182d275f5c3c1c668866e791efa9'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #relative path from current file
db = SQLAlchemy() #DB instance db strucuture is proposed as classes or models
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' #function name of the route
login_manager.login_message_category = 'info'

mail = Mail()




def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    app.register_blueprint(users)

    from flaskblog.posts.routes import posts
    app.register_blueprint(posts)

    from flaskblog.main.routes import main
    app.register_blueprint(main)
    
    from flaskblog.errors.handlers import errors
    app.register_blueprint(errors)

    return app
    