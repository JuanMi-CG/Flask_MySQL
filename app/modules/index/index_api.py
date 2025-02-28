from flask import render_template, request, redirect, url_for, flash
from app import db
from app.models.usuarios import Usuario
from . import index_bp
from werkzeug.security import generate_password_hash

# Redirige la ruta raíz a la gestión de usuarios
@index_bp.route('/')
def index():
    return redirect(url_for('index.usuarios'))

# Muestra la lista de usuarios y el formulario (de creación o edición)
@index_bp.route('/usuarios', methods=['GET'])
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

# Crea un nuevo usuario
@index_bp.route('/usuarios/create', methods=['POST'])
def usuarios_create():
    nombre = request.form['nombre']
    email = request.form['email']
    contraseña = request.form['contraseña']
    nuevo_usuario = Usuario(nombre, email, contraseña)
    db.session.add(nuevo_usuario)
    db.session.commit()
    flash('Usuario creado correctamente', 'success')
    return redirect(url_for('index.usuarios'))

# Edita un usuario existente
@index_bp.route('/usuarios/edit/<int:id>', methods=['GET', 'POST'])
def usuarios_edit(id):
    usuario = Usuario.query.get_or_404(id)
    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.email = request.form['email']
        new_password = request.form.get('contraseña')
        if new_password:
            usuario.contraseña_hash = generate_password_hash(new_password)
        db.session.commit()
        flash('Usuario actualizado correctamente', 'success')
        return redirect(url_for('index.usuarios'))
    # En el GET se pasa el usuario a editar junto con la lista completa para mostrar el CRUD
    return render_template('index.html', usuario_editar=usuario, usuarios=Usuario.query.all())

# Elimina un usuario
@index_bp.route('/usuarios/delete/<int:id>', methods=['POST'])
def usuarios_delete(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado correctamente', 'success')
    return redirect(url_for('index.usuarios'))
