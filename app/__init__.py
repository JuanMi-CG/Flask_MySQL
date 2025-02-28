
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
import os, importlib
import sys
import inspect

# Instancias globales de las extensiones
db = SQLAlchemy()
# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tu_secret_key_aqui'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://remoto:Remoto123!@db/ERP'
    
    db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view = 'login.login'

    # Registro automático de blueprints
    modules_dir = os.path.join(os.path.dirname(__file__), 'modules')
    for module_name in os.listdir(modules_dir):
        module_path = os.path.join(modules_dir, module_name)
        if os.path.isdir(module_path) and not module_name.startswith('__'):
            try:
                mod = importlib.import_module(f'app.modules.{module_name}')
                blueprint = getattr(mod, f'{module_name}_bp', None)
                if blueprint:
                    app.register_blueprint(blueprint)
                    print(f"Blueprint '{module_name}_bp' registrado.")
                else:
                    print(f"No se encontró '{module_name}_bp' en app.modules.{module_name}")
            except Exception as e:
                print(f"Error al registrar el blueprint del módulo '{module_name}': {e}")

    # Registro automático de modelos
    models_dir = os.path.join(os.path.dirname(__file__), 'models')
    for filename in os.listdir(models_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # elimina la extensión .py
            importlib.import_module(f'app.models.{module_name}')
            print(f'Modelo cargado: {module_name}')

    @app.route('/')
    def raiz():
        return redirect('/index/')

    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('home.home'))

    with app.app_context():
        db.create_all()

    return app