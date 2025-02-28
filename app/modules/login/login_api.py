from flask import render_template
from . import login_bp

@login_bp.route('/')
def login():
    return render_template('login.html')
