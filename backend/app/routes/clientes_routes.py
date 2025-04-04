from flask import Blueprint, request, jsonify
from ..services.clientes_service import cadastrar_cliente, consultar_cliente, atualizar_cliente, deletar_cliente    

clientes_bp = Blueprint('clientes', __name__)

#ENDPOINT PARA CADASTRAR CLIENTE
@clientes_bp.route('/', methods=['POST'])#ENDPOINT PARA CADASTRO.
def endpoint_cadastrar_cliente():

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

#ENDPOINT PARA CONSULTA TANTO COM ID QUANTO COM CNPJ
@clientes_bp.route('/', methods=['GET'])
def endpoint_consultar_cliente():
    id = request.args.get('id', type=int)
    cnpj = request.args.get('cnpj', type=str)

    try:
        cliente = consultar_cliente(id=id, cnpj=cnpj)
        return jsonify({
            "id": cliente.id,
            "cnpj": cliente.cnpj,
            "razao_social": cliente.razao_social,
            "nome_fantasia": getattr(cliente, "nome_fantasia", None),
            "email": getattr(cliente, "email", None)
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
'''
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
        return jsonify({"erro": str(e)}), 404'
'''
#ENDPOINT PARA ATUALIZAR CLIENTE
@clientes_bp.route('/<int:id>', methods=['PUT'])
def endpoint_atualizar_cliente(id):
    try:
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Nenhum dado fornecido para atualização"}), 400

        # Chama a função de serviço
        cliente_atualizado = atualizar_cliente(id, dados)

        # Resposta com os campos atualizados
        return jsonify({
            "mensagem": "Cliente atualizado com sucesso",
            "id": cliente_atualizado.id,
            "campos_alterados": list(dados.keys())
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Cliente não encontrado ou dados inválidos

    except Exception as e:
        return jsonify({"erro": f"Falha na atualização: {str(e)}"}), 500
    

#ENDPOINT PARA DELETAR CLIENTE:
@clientes_bp.route('/<int:id>', methods=['DELETE'])
def endpoint_deletar_cliente(id):
    try:
        sucesso = deletar_cliente(id)  # Chama a função de serviço
        
        if sucesso:
            return jsonify({
                "mensagem": "Cliente desativado com sucesso",
                "id": id,
                "status": "inativo"
            }), 200
    
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Cliente não encontrado ou já inativo
    
    except Exception as e:
        return jsonify({"erro": f"Falha ao desativar cliente: {str(e)}"}), 500