from flask import Flask
from config import config
from .extensions import db, migrate, jwt

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Carregar configurações CORRETAMENTE
    app.config.from_object(config[config_name])
    
    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    
    # Registrar blueprints
    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app