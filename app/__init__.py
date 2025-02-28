from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Cargar configuraciones, si es necesario
    # app.config.from_object('config.Config')
    
    # Registrar blueprints de cada módulo
    from app.modules.index import index_bp
    from app.modules.home import home_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(home_bp)
    
    return app
