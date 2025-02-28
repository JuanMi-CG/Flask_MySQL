from flask import render_template
from . import home_bp

@home_bp.route('/')
def home():
    return render_template('home.html')

@home_bp.route('/api/home')
def asd():
    return 'asdf'