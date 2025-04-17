from ..extensions import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..models.user import User
from ..services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados inválidos"}), 400
            
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()
        
        if not user or not user.check_password(password):
            return jsonify({"error": "Credenciais inválidas"}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({
            "access_token": access_token,
            "user": {
                "id": user.id,
                "username": user.username
            }
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Erro no servidor",
            "message": str(e)
        }), 500
    
@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados inválidos"}), 400

        username = data.get('username')
        cpf = data.get('cpf')
        password = data.get('password')

        if not username or not cpf or not password:
            return jsonify({"error": "Os campos username, cpf e password são obrigatórios"}), 400

        new_user, error = AuthService.create_user(username, cpf, password)
        if error:
            return jsonify({"error": error}), 400

        return jsonify({
            "message": "Usuário cadastrado com sucesso",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "cpf": new_user.cpf
            }
        }), 201

    except Exception as e:
        return jsonify({
            "error": "Erro no servidor",
            "message": str(e)
        }), 500