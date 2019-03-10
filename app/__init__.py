from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma


def create_app(): #factory
    #configura app
    app = Flask(__name__)

    #configura SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/crud.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #Configura banco e serializer
    config_db(app)
    config_ma(app)

    #Migração
    Migrate(app, app.db)

    from .books import bp_books
    app.register_blueprint(bp_books)

    return app
