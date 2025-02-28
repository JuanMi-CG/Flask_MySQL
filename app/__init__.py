from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__)
    
    # Registrar blueprints
    from app.modules.index import index_bp
    from app.modules.home import home_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(home_bp)
    
    # Manejador de error 404: redirige a la ruta home
    @app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('home.home'))
    
    @app.route('/')
    def raiz():
        return redirect('/index/')


    
    return app
