from flask import Flask, jsonify, request

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Ilokano to Tagalog Machine Translation'
    
    from .views import views
    
    app.register_blueprint(views, url_prefix='/')
    
    return app
