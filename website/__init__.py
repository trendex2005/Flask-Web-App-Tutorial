import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key' # Use a real key in Config Vars later
    
    # FIX: Heroku uses 'postgres://', but SQLAlchemy 1.4+ needs 'postgresql://'
    uri = os.getenv("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = uri or f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Register blueprints and models here as you did before...
    
    with app.app_context():
        db.create_all() # This creates the tables on Heroku's database

    return app
