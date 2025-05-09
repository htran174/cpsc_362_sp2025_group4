import os
import stripe

from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'temporary_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    stripe.api_key = os.environ['STRIPE_SECRET_KEY']

    from .views import views
    from .auth import auth
    from .checkout import checkout

    from .models import User, Payment, Product

    with app.app_context():
        create_database()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    app.register_blueprint(views, urlprefix='/')
    app.register_blueprint(auth, urlprefix='/')
    app.register_blueprint(checkout, urlprefix='/')

    return app

def create_database():
    if not path.exists(f'website/{DB_NAME}'):
        db.create_all()
        print('Database created!')