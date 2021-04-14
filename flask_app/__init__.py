from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_pyfile('../config.cfg')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

import flask_app.admin
