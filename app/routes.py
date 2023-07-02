from flask import render_template
from app import app
from app.models import *

@app.route('/')
def index():
    return '<h1 style = "color:red">Hello, World!</h1>'
