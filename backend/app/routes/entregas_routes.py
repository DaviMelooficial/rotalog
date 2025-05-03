from ..extensions import Blueprint,request, jsonify
from ..services.entregas_service import cadastrar_entrega, consultar_entrega, atualizar_entrega, listar_entregas, cancelar_entrega

entregas_bp = Blueprint('entregas', __name__)


#CADASTRAR ENTREGAS
@entregas_bp.route('/cadastrar_entrega', methods=['POST'])
def cadastrar_entrega_endpoint():
    try:
        dados = request.get_json()
        
        # Validação básica
        if not dados.get('cnpj_cliente') or not dados.get('nota_fiscal'):
            return jsonify({"erro": "CNPJ do cliente e nota fiscal são obrigatórios"}), 400

        entrega = cadastrar_entrega(dados)
        
        return jsonify({
            "mensagem": "Entrega cadastrada com sucesso",
            "id_entrega": entrega.id_entrega,
            "nota_fiscal": entrega.nota_fiscal
        }), 201

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Bad Request (dados inválidos)
    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
    

#CONSULTAR ENTREGAS
@entregas_bp.route('/consultar_entrega', methods=['GET'])  
def consultar_entrega_endpoint():
    try:
        # Obtém a nota fiscal da requisição
        nota_fiscal = request.args.get('nota_fiscal')

        if not nota_fiscal:
            return jsonify({"erro": "Nota fiscal não fornecida"}), 400

        # Consulta a entrega pelo número da nota fiscal
        entrega = consultar_entrega(nota_fiscal)

        # Retorna os dados da entrega
        return jsonify({
            "id": entrega.id_entrega,
            "cnpj_cliente": entrega.cnpj_cliente,
            "nota_fiscal": entrega.nota_fiscal,
            "logradouro_entrega": entrega.logradouro_entrega,
            "bairro_entrega": entrega.bairro_entrega,
            "cidade_entrega": entrega.cidade_entrega,
            "estado_entrega": entrega.estado_entrega,
            "cep_entrega": entrega.cep_entrega,
            "volume": entrega.volume,
            "data_entrega": entrega.data_entrega.strftime('%Y-%m-%d'),
            "status": "Vinculada" if hasattr(entrega, "ROTA") and entrega.ROTA else "Pendente"
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Entrega não encontrada
    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500    

@entregas_bp.route('/listar_entregas', methods=['GET'])
def listar_entregas_endpoint():
    try:
        entregas = listar_entregas()
        
        if not entregas:
            return jsonify({"mensagem": "Nenhuma entrega encontrada"}), 404
        
        entregas_list = []
        for entrega in entregas:
            entregas_list.append({
                "id": entrega.id_entrega,
                "cnpj_cliente": entrega.cnpj_cliente,
                "nota_fiscal": entrega.nota_fiscal,
                "logradouro_entrega": entrega.logradouro_entrega,
                "bairro_entrega": entrega.bairro_entrega,
                "cidade_entrega": entrega.cidade_entrega,
                "estado_entrega": entrega.estado_entrega,
                "cep_entrega": entrega.cep_entrega,
                "volume": entrega.volume,
                "data_entrega": entrega.data_entrega.strftime('%Y-%m-%d'),
                "status": "Vinculada" if hasattr(entrega, "ROTA") and entrega.ROTA else "Pendente"
            })
        
        return jsonify(entregas_list), 200

    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
#ATUALIZAR ENTREGAS
@entregas_bp.route('/atualizar_entrega/<string:nota_fiscal>', methods=['PUT'])
def atualizar_entrega_endpoint(nota_fiscal):
    try:
        dados = request.get_json()
        
        if not dados:
            return jsonify({"erro": "Nenhum dado fornecido"}), 400

        entrega = atualizar_entrega(nota_fiscal, dados)
        
        return jsonify({
            "mensagem": "Entrega atualizada",
            "campos_alterados": list(dados.keys())
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 404  # Not Found
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
    


@entregas_bp.route('/cancelar_entrega/<string:nota_fiscal>', methods=['PATCH'])
def cancelar_entrega_endpoint(nota_fiscal):
    try:
        entrega = cancelar_entrega(nota_fiscal)
        return jsonify({
            "mensagem": "Entrega cancelada com sucesso",
            "nota_fiscal": entrega.nota_fiscal,
            "status": entrega.status_entrega
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500   
