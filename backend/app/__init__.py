from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from config import config
from .extensions import db, migrate, jwt

def create_app(config_name='development'):
    app = Flask(__name__)
    
    # Configuração CORS aprimorada
    cors = CORS(app, resources={r"/*": {
        "origins": ["http://localhost:5173", "http://localhost:8080"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }})

    # Configurações principais
    app.config.from_object(config[config_name])
    
    # Inicialização de extensões
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    """
    # Handler para requisições OPTIONS (pré-flight)
    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            response = make_response()
            response.headers.add("Access-Control-Allow-Origin", 
                               app.config.get("CORS_ORIGIN", "http://localhost:5173"))
            response.headers.add("Access-Control-Allow-Headers", 
                               "Content-Type, Authorization")
            response.headers.add("Access-Control-Allow-Methods", 
                               "GET, POST, PUT, DELETE, OPTIONS")
            return response
    """
    
    # Registrar blueprints
    from .routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from .routes.clientes_routes import clientes_bp
    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    from .routes.veiculos_routes import veiculos_bp
    app.register_blueprint(veiculos_bp, url_prefix='/veiculos')
    from .routes.motorista_routes import motoristas_bp
    app.register_blueprint(motoristas_bp, url_prefix='/motoristas')
    from .routes.entregas_routes import entregas_bp
    app.register_blueprint(entregas_bp, url_prefix='/entregas')

    # Error handler global
    @app.errorhandler(500)
    def handle_server_error(e):
        return jsonify({
            "error": "Internal server error",
            "message": str(e)
        }), 500

    return app