from ..extensions import Blueprint, request, jsonify
from ..services.veiculos_service import (
    cadastrar_veiculos,
    consultar_veiculo,
    atualizar_veiculo,
    cancelar_veiculo,
    listar_veiculos
)

# Criação do Blueprint para as rotas de veículos
veiculos_bp = Blueprint('veiculos', __name__, url_prefix='/veiculos')

# Rota para cadastrar um veículo
@veiculos_bp.route('/cadastrar', methods=['POST'])
def cadastrar():
    dados = request.get_json()
    try:
        resultado = cadastrar_veiculos(dados)
        return jsonify(resultado), 201
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

# Rota para consultar um veículo por ID ou placa
@veiculos_bp.route('/consultar', methods=['GET'])
def consultar():
    id_veiculo = request.args.get('id_veiculo')
    placa = request.args.get('placa')
    try:
        veiculo = consultar_veiculo(id_veiculo=id_veiculo, placa=placa)
        if veiculo:
            return jsonify({
                "ID_VEICULO": veiculo.ID_VEICULO,
                "PLACA": veiculo.PLACA,
                "MARCA": veiculo.MARCA,
                "MODELO": veiculo.MODELO,
                "COR": veiculo.COR,
                "ANO_FABRICACAO": veiculo.ANO_FABRICACAO,
                "RENAVAM": veiculo.RENAVAM,
                "CHASSI": veiculo.CHASSI,
                "TIPO_CARROCERIA": veiculo.TIPO_CARROCERIA,
                "CAPACIDADE_CARGA": veiculo.CAPACIDADE_CARGA,
                "STATUS": veiculo.STATUS
            }), 200
        return jsonify({"erro": "Veículo não encontrado"}), 404
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

# Rota para listar todos os veículos
@veiculos_bp.route('/listar', methods=['GET'])
def listar():
    try:
        # Chama a função de serviço para listar os veículos
        veiculos = listar_veiculos()

        # Converte os veículos para um formato serializável
        veiculos_serializados = [
            {
                "ID_VEICULO": veiculo.ID_VEICULO,
                "PLACA": veiculo.PLACA,
                "MARCA": veiculo.MARCA,
                "MODELO": veiculo.MODELO,
                "COR": veiculo.COR,
                "ANO_FABRICACAO": veiculo.ANO_FABRICACAO,
                "RENAVAM": veiculo.RENAVAM,
                "CHASSI": veiculo.CHASSI,
                "TIPO_CARROCERIA": veiculo.TIPO_CARROCERIA,
                "CAPACIDADE_CARGA": veiculo.CAPACIDADE_CARGA,
                "STATUS": veiculo.STATUS
            }
            for veiculo in veiculos
        ]

        return jsonify(veiculos_serializados), 200

    except Exception as e:
        return jsonify({"erro": f"Falha ao listar veículos: {str(e)}"}), 500

# Rota para atualizar um veículo
@veiculos_bp.route('/atualizar/<int:id_veiculo>', methods=['PUT'])
def atualizar(id_veiculo):
    dados = request.get_json()
    try:
        veiculo = atualizar_veiculo(id_veiculo, dados)
        return jsonify({
            "mensagem": f"Veículo de ID {id_veiculo} atualizado com sucesso.",
            "veiculo": {
                "ID_VEICULO": veiculo.ID_VEICULO,
                "PLACA": veiculo.PLACA,
                "MARCA": veiculo.MARCA,
                "MODELO": veiculo.MODELO,
                "COR": veiculo.COR,
                "ANO_FABRICACAO": veiculo.ANO_FABRICACAO,
                "RENAVAM": veiculo.RENAVAM,
                "CHASSI": veiculo.CHASSI,
                "TIPO_CARROCERIA": veiculo.TIPO_CARROCERIA,
                "CAPACIDADE_CARGA": veiculo.CAPACIDADE_CARGA,
                "STATUS": veiculo.STATUS
            }
        }), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

# Rota para cancelar (desativar) um veículo
@veiculos_bp.route('/cancelar/<int:id_veiculo>', methods=['PUT'])
def cancelar(id_veiculo):
    try:
        resultado = cancelar_veiculo(id_veiculo)
        return jsonify(resultado), 200
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400
    
    