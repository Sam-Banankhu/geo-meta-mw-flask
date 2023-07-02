from flask import Flask

app = Flask(__name__)

# Import the routes
from app import routes
