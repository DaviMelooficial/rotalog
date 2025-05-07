from ..extensions import Blueprint, request, jsonify, db
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
def user_register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados inválidos"}), 400

        name = data.get('name')
        cpf = data.get('cpf')
        email = data.get('email')
        position = data.get('position')
        username = data.get('username')
        password = AuthService.generate_password()

        if not all([name, email, cpf, position, username, password]):
            return jsonify({"error": "Todos os campos são obrigatórios"}), 40
        
        new_user, error = AuthService.create_user(
            name=name,
            cpf=cpf,
            email=email,
            position=position,
            username=username,
            password=password
        )
        if error:
            return jsonify({"error": error}), 400

        return jsonify({
            "message": "Usuário cadastrado com sucesso",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "cpf": new_user.cpf,
                "email": new_user.email,
                "position": new_user.position
            }
        }), 201

    except Exception as e:
        return jsonify({
            "error": "Erro no servidor",
            "message": str(e)
        }), 500

@auth_bp.route('/forgot_password', methods=['POST'])
def forgot_password():
    try:
        data = request.get_json()
        if not data or 'cpf' not in data:
            return jsonify({"error": "CPF é obrigatório"}), 400

        cpf = data['cpf']
        
        try:
            AuthService.forgot_password(cpf)
            return jsonify({"message": "Um link para redefinição de senha foi enviado para seu email"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404

    except Exception as e:
        return jsonify({
            "error": "Erro no servidor",
            "message": str(e)
        }), 500

@auth_bp.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
    try:
        data = request.get_json()
        if not data or 'new_password' not in data:
            return jsonify({"error": "Nova senha não fornecida"}), 400

        new_password = data['new_password']
        
        try:
            AuthService.reset_password(token, new_password)
            return jsonify({"message": "Senha redefinida com sucesso"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

    except Exception as e:
        return jsonify({
            "error": "Erro no servidor",
            "message": str(e)
        }), 500

@auth_bp.route('/consult_user/<string:cpf>', methods=['GET'])
def user_consult(cpf):
    try:
        user = AuthService.consult_user(cpf=cpf)
        return jsonify({
            "id": user.id,
            "status": user.status,
            "cpf": user.cpf,
            "email": user.email,
            "name": user.name,
            "password": user.password_hash,
            "position": user.position
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

@auth_bp.route('/consult_user', methods=['GET'])
def user_consult_query():
    try:
        cpf = request.args.get('cpf')
        email = request.args.get('email')
        name = request.args.get('name')

        if not any([cpf, email, name]):
            return jsonify({"error": "Pelo menos um parâmetro de consulta (cpf, email, name) deve ser fornecido"}), 400

        user = AuthService.consult_user_by_query(cpf=cpf, email=email, name=name)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404

        return jsonify({
            "id": user.id,
            "status": user.status,
            "cpf": user.cpf,
            "email": user.email,
            "name": user.name,
            "position": user.position
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": "Erro no servidor", "message": str(e)}), 500

@auth_bp.route('/list_users', methods=['GET'])
def user_list():
    try:
        users = AuthService.list_users()
        return jsonify([{
            "id": user.id,
            "status": user.status,
            "cpf": user.cpf,
            "email": user.email,
            "name": user.name,
            "password": user.password_hash,
            "position": user.position
        } for user in users]), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    
@auth_bp.route('/update_user/<string:cpf>', methods=['PUT'])
def user_update(cpf):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Nenhum dado fornecido para atualização"}), 400

        user_updated = AuthService.update_user(cpf, data)

        return jsonify({
            "message": "Usuário atualizado com sucesso",
            "cpf": user_updated.cpf,
            "fields_updated": list(data.keys())
        }), 200

    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@auth_bp.route('/disable_user/<string:cpf>', methods=['PATCH'])
def user_disable(cpf):
    try:
        AuthService.disable_user(cpf)
        return jsonify({"message": "Usuário desativado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@auth_bp.route('/enable_user/<string:cpf>', methods=['PATCH'])    
def user_enable(cpf):
    try:
        AuthService.reactivate_user(cpf)
        return jsonify({"message": "Usuário reativado com sucesso"}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
