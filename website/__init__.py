from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET _KEY'] = '412ValStats'

    from .views import views

    app.register_blueprint(views, url_prefix='/')

    return app
