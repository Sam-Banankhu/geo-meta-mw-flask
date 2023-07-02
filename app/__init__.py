from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Create the Flask application instance
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from app import routes, models

# Ensure that the database tables are created
with app.app_context():
    db.create_all()
