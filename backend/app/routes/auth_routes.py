from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ..services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    cpf = data.get('cpf')
    password = data.get('password')

    if not all([username, cpf, password]):
        return jsonify({'error': 'Missing required fields'}), 400

    user, error = AuthService.create_user(username, cpf, password)
    if error:
        return jsonify({'error': error}), 400

    return jsonify({
        'message': 'User created successfully',
        'user': {
            'id': user.id,
            'username': user.username,
            'cpf': user.cpf
        }
    }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user, error = AuthService.authenticate_user(username, password)
    if error:
        return jsonify({'error': error}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({
        'access_token': access_token,
        'user': {
            'id': user.id,
            'username': user.username,
            'cpf': user.cpf
        }
    }), 200