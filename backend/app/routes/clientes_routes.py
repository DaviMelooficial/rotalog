from flask import Blueprint, request, jsonify
from ..services.clientes_service import cadastrar_cliente, consultar_cliente
from ..models import Cliente  # Para a consulta

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['POST'])#ENDPOINT PARA CADASTRO.
def endpoint_cadastrar_cliente():
    """
    Endpoint HTTP para cadastro de clientes.
    """
    try:
        dados = request.get_json()
        
        # Chama a função pura
        cliente = cadastrar_cliente(dados)
        
        # Resposta de sucesso
        return jsonify({
            "mensagem": "Cliente cadastrado com sucesso",
            "id": cliente.id,
            "cnpj": cliente.cnpj
        }), 201
    
    except ValueError as e:
        # Erros de validação (400 Bad Request)
        return jsonify({"erro": str(e)}), 400
    
    except Exception as e:
        # Erros inesperados (500 Internal Server Error)
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
    



# Consulta por ID
@clientes_bp.route('/clientes/<int:id>', methods=['GET'])
def endpoint_consultar_cliente_por_id(id):
    try:
        cliente = consultar_cliente(id=id)
        return jsonify({
            "id": cliente.id,
            "cnpj": cliente.cnpj,
            "razao_social": cliente.razao_social,
            "email": cliente.email
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404



# Consulta por CNPJ
@clientes_bp.route('/clientes/cnpj/<string:cnpj>', methods=['GET'])
def endpoint_consultar_cliente_por_cnpj(cnpj):
    try:
        cliente = consultar_cliente(cnpj=cnpj)
        return jsonify({
            "id": cliente.id,
            "cnpj": cliente.cnpj,
            "nome_fantasia": cliente.nome_fantasia
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404