from ..extensions import Blueprint, request, jsonify
from ..services.motoristas_service import cadastrar_motorista, consultar_motorista, atualizar_motorista, cancelar_motorista, listar_motoristas

motoristas_bp = Blueprint('motoristas', __name__)

@motoristas_bp.route('/cadastrar_motorista', methods=['POST']) #CRIAR MOTORISTA
def cadastrar_motorista_endpoint():
    try:
        dados = request.get_json()
        
        # Validação básica
        if not dados.get('nome_motorista') or not dados.get('cpf') or not dados.get('cnh'):
            return jsonify({"erro": "Nome do motorista, CPF e CNH são obrigatórios"}), 400

        motorista = cadastrar_motorista(dados)
        
        return jsonify({
            "mensagem": "Motorista cadastrado com sucesso",
            "id_motorista": motorista.get("id_motorista"),
            "nome_motorista": motorista.get("nome_motorista")
        }), 201

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Bad Request (dados inválidos)
    except Exception as e:
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
    

@motoristas_bp.route('/consultar_motorista', methods=['GET']) #CONSULTAR MOTORISTA
def consultar_motorista_endpoint():
    try:    
        id_motorista = request.args.get('id_motorista')
        cnh = request.args.get('cnh')

        motorista = consultar_motorista(
            id_motorista=int(id_motorista) if id_motorista else None,
            cnh=cnh
        )

        if not motorista:
            return jsonify({"erro": "Motorista não encontrado"}), 404

        return jsonify({
            "id_motorista": motorista.Id_motorista,
            "nome_motorista": motorista.nome_motorista,
            "cpf": motorista.CPF,
            "cnh": motorista.CNH,
            "classificacao": motorista.classificacao,
            "telefone": motorista.Telefone
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
   

@motoristas_bp.route('/atualizar_motoristas/<int:id_motorista>', methods=['PUT']) #ATUALIZAR MOTORISTA
def atualizar_motorista_endpoint(id_motorista):
    try:
        dados = request.get_json()
        
        motorista = atualizar_motorista(id_motorista, dados)

        return jsonify({
            "mensagem": "Motorista atualizado com sucesso",
            "id_motorista": motorista.id_motorista,
            "nome_motorista": motorista.nome_motorista
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Bad Request (dados inválidos)
    except Exception as e:  
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500       
    

@motoristas_bp.route('/motoristas/<int:id_motorista>', methods=['DELETE']) #CANCELAR MOTORISTA
def cancelar_motorista_endpoint(id_motorista):
    try:
        sucesso = cancelar_motorista(id_motorista)

        if not sucesso:
            return jsonify({"erro": "Motorista não encontrado"}), 404

        return jsonify({
            "mensagem": "Motorista cancelado com sucesso"
        }), 200

    except ValueError as e:
        return jsonify({"erro": str(e)}), 400  # Bad Request (dados inválidos)
    except Exception as e:  
        return jsonify({"erro": f"Falha no servidor: {str(e)}"}), 500
    
@motoristas_bp.route('/listar_motoristas', methods=['GET'])  # LISTAR MOTORISTAS
def listar_motoristas_endpoint():
    try:
        # Chama a função de serviço para listar os motoristas
        motoristas = listar_motoristas()

        # Converte os motoristas para um formato serializável
        motoristas_serializados = [
            {
                "id_motorista": motorista.id_motorista,
                "nome_motorista": motorista.nome_motorista,
                "cpf": motorista.cpf,
                "cnh": motorista.cnh,
                "classificacao": motorista.classificacao,
                "telefone": motorista.telefone
            }
            for motorista in motoristas
        ]

        return jsonify(motoristas_serializados), 200

    except Exception as e:
        return jsonify({"erro": f"Falha ao listar motoristas: {str(e)}"}), 500