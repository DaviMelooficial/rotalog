from flask import Blueprint, request, jsonify
from ..services.clientes_service import cadastrar_cliente, consultar_cliente, atualizar_cliente, desativar_cliente, listar_clientes 

clientes_bp = Blueprint('clientes', __name__)

#ENDPOINT PARA CADASTRAR CLIENTE
@clientes_bp.route('/cadastrar_cliente', methods=['POST'])#ENDPOINT PARA CADASTRO.
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

#ENDPOINT PARA CONSULTA COM CNPJ
@clientes_bp.route('/consultar_cliente/<string:cnpj>', methods=['GET'])
def endpoint_consultar_cliente(cnpj):
    try:
        cliente = consultar_cliente(cnpj=cnpj)
        return jsonify({
            "id": cliente.id,
            "cnpj": cliente.cnpj,
            "razao_social": cliente.razao_social,
            "nome_fantasia": getattr(cliente, "nome_fantasia", None),
            "status": cliente.status,
            "telefone": cliente.telefone,
            "email": getattr(cliente, "email", None)
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

#ENDPOINT PARA ATUALIZAR CLIENTE
@clientes_bp.route('/atualizar_cliente/<string:cnpj>', methods=['PUT'])
def endpoint_atualizar_cliente(cnpj):
    try:
        dados = request.get_json()

        if not dados:
            return jsonify({"erro": "Nenhum dado fornecido para atualização"}), 400

        # Chama a função de serviço
        cliente_atualizado = atualizar_cliente(cnpj, dados)

        # Resposta com os campos atualizados
        return jsonify({
            "mensagem": "Cliente atualizado com sucesso",
            "cnpj": cliente_atualizado.cnpj,
            "campos_alterados": list(dados.keys())
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Cliente não encontrado ou dados inválidos

    except Exception as e:
        return jsonify({"erro": f"Falha na atualização: {str(e)}"}),     500
    

#ENDPOINT PARA DESATIVAR CLIENTE:
@clientes_bp.route('/desativar_cliente/<string:cnpj>', methods=['PATCH'])
def endpoint_desativar_cliente(cnpj):
    try:
        cliente = desativar_cliente(cnpj)  # Chama a função para desativar o cliente
        return jsonify({
            "mensagem": f"Cliente {cliente.razao_social} desativado com sucesso.",
            "cnpj": cliente.cnpj,
            "status": cliente.status
        }), 200  # Retorna o cliente com o status e cadastro travado
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Retorna erro se cliente não encontrado ou já inativo
    except Exception as e:
        return jsonify({"erro": str(e)}), 500  # Retorna erro genérico se houver falha no processo

# ENDPOINT PARA LISTAR TODOS OS CLIENTES
@clientes_bp.route('/listar_clientes', methods=['GET'])
def endpoint_listar_clientes():
    try:
        # Chama a função de serviço para listar os clientes
        clientes = listar_clientes()

        # Converte os clientes para um formato serializável
        clientes_serializados = [
            {
                "id": cliente.id,
                "cnpj": cliente.cnpj,
                "razao_social": cliente.razao_social,
                "nome_fantasia": getattr(cliente, "nome_fantasia", None),
                "status": cliente.status,
                "telefone": cliente.telefone,
                "email": getattr(cliente, "email", None)
            }
            for cliente in clientes
        ]

        return jsonify(clientes_serializados), 200

    except Exception as e:
        return jsonify({"erro": f"Falha ao listar clientes: {str(e)}"}), 500