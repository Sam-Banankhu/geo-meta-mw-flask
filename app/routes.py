from app import app

@app.route('/')
def index():
    return '<h1 style = "color:red">Hello, World!</h1>'
