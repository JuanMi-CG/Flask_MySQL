from flask import request, jsonify, render_template, send_file, current_app
import os
from app import db
from app.models.usuarios import Usuario
from . import index_bp
from werkzeug.security import generate_password_hash

# Sirve la aplicación SPA (frontend estático)
@index_bp.route('/')
def index():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html'))


# API: Obtener la lista de usuarios
@index_bp.route('/api/usuarios', methods=['GET'])
def api_get_usuarios():
    usuarios = Usuario.query.all()
    usuarios_data = []
    for u in usuarios:
        usuarios_data.append({
            'id': u.id,
            'nombre': u.nombre,
            'email': u.email,
            'fecha_creacion': u.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify({'usuarios': usuarios_data})

# API: Crear un usuario
@index_bp.route('/api/usuarios', methods=['POST'])
def api_create_usuario():
    data = request.json
    nombre = data.get('nombre')
    email = data.get('email')
    contraseña = data.get('contraseña')
    if not all([nombre, email, contraseña]):
        return jsonify({'message': 'Datos incompletos'}), 400
    nuevo_usuario = Usuario(nombre, email, contraseña)
    db.session.add(nuevo_usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario creado correctamente'})

# API: Actualizar un usuario
@index_bp.route('/api/usuarios/<int:id>', methods=['PUT'])
def api_update_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    data = request.json
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.email = data.get('email', usuario.email)
    new_password = data.get('contraseña')
    if new_password:
        usuario.contraseña_hash = generate_password_hash(new_password)
    db.session.commit()
    return jsonify({'message': 'Usuario actualizado correctamente'})

# API: Eliminar un usuario
@index_bp.route('/api/usuarios/<int:id>', methods=['DELETE'])
def api_delete_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'message': 'Usuario eliminado correctamente'})
