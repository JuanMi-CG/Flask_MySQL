from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.user import User
from app import db

# Al usar template_folder="." se buscará login.html en el mismo directorio que este archivo
login_bp = Blueprint('login', __name__, url_prefix='/login', template_folder='.')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash("Sesión iniciada correctamente", "success")
            return redirect(url_for('home.home'))  # Redirige a la home u otra ruta protegida
        else:
            flash("Credenciales inválidas", "danger")
    return render_template('login.html')

@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Has cerrado sesión", "success")
    return redirect(url_for('login.login'))
