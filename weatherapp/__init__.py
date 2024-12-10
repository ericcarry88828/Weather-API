from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')

    from . import weather
    app.register_blueprint(weather.bp)
    return app
