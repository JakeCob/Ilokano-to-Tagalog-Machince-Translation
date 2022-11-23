from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_TL_IL = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ilokano to Tagalog Machine Translation'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_TL_IL}'
    db.init_app(app)
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app
