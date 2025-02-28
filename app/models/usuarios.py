from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla en la base de datos

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    contraseña_hash = db.Column(db.String(256), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña_hash = generate_password_hash(contraseña)  # Hashea la contraseña

    def verificar_contraseña(self, contraseña):
        return check_password_hash(self.contraseña_hash, contraseña)  # Verifica la contraseña

    def __repr__(self):
        return f'<Usuario {self.nombre} ({self.email})>'
