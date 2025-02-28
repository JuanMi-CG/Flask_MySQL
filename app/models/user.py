from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    usuario = User(username='admin', email='admin@example.com')
    usuario.set_password('tu_contraseña')
    db.session.add(usuario)
    db.session.commit()
