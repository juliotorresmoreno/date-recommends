
from app import app

def index():
    return "hello"

def configure():
    app.route('/')(index)
