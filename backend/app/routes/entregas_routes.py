from flask import Blueprint, request, jsonify
from  ..services.entregas_service import cadastrar_entrega, consultar_entrega, atualizar_entrega, cancelar_entrega

entregas_bp = Blueprint('clientes', __name__)



@entregas_bp.route('/entregas', methods=['POST'])#CRIAR ENTREGAS
def cadastrar_entrega_endpoint():
    try:
        dados = request.get_json()
        
        # Validação básica
        if not dados.get('cnpj_cliente') or not dados.get('nota_fiscal'):
            return jsonify({"erro": "CNPJ do cliente e nota fiscal são obrigatórios"}), 400

        entrega = cadastrar_entrega(dados)
        
        return jsonify({
            "mensagem": "Entrega cadastrada com sucesso",
            "id_entrega": entrega.ID_ENTREGA,
            "nota_fiscal": entrega.NOTA_FISCAL
        }), 201

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Bad Request (dados inválidos)
    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
    


@entregas_bp.route('/entregas', methods=['GET'])#CONSULTAR ENTREGAS
def consultar_entrega_endpoint():
    try:
        id_entrega = request.args.get('id')
        nota_fiscal = request.args.get('nota_fiscal')

        entrega = consultar_entrega(
            id_entrega=int(id_entrega) if id_entrega else None,
            nota_fiscal=nota_fiscal
        )

        if not entrega:
            return jsonify({"erro": "Entrega não encontrada"}), 404

        return jsonify({
            "id": entrega.ID_ENTREGA,
            "cnpj_cliente": entrega.CNPJ_CLIENTE,
            "nota_fiscal": entrega.NOTA_FISCAL,
            "status": "Vinculada" if entrega.ROTA else "Pendente"
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    


@entregas_bp.route('/entregas/<int:id_entrega>', methods=['PUT'])#ATUALIZAR ENTREGAS
def atualizar_entrega_endpoint(id_entrega):
    try:
        dados = request.get_json()
        
        if not dados:
            return jsonify({"erro": "Nenhum dado fornecido"}), 400

        entrega = atualizar_entrega(id_entrega, dados)
        
        return jsonify({
            "mensagem": "Entrega atualizada",
            "campos_alterados": list(dados.keys())
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Not Found
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    


@entregas_bp.route('/entregas/<int:id_entrega>', methods=['DELETE'])
def cancelar_entrega_endpoint(id_entrega):
    try:
        sucesso = cancelar_entrega(id_entrega)
        
        if sucesso:
            return jsonify({
                "mensagem": "Entrega desvinculada da rota",
                "id_entrega": id_entrega
            }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500    
