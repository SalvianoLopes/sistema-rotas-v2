# app/__init__.py
from flask import Flask
from app.db import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app

