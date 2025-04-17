from ..extensions import db
from ..models import Veiculo
from ..extensions import datetime


#CADASTRAR VEÍCULO
def cadastrar_veiculos(dados_veiculo):
    if Veiculo.query.filter_by(PLACA=dados_veiculo['placa']).first():
        raise ValueError("Veículo já cadastrado")
    

    novo_veiculo = Veiculo(
        PLACA=dados_veiculo['placa'],
        MARCA=dados_veiculo['marca'],
        MODELO=dados_veiculo['modelo'],
        COR=dados_veiculo['cor'],
        ANO_FABRICACAO=dados_veiculo['ano_fabricacao'],
        RENAVAM=dados_veiculo['renavam'],
        CHASSI=dados_veiculo['chassi'],
        TIPO_CARROCERIA=dados_veiculo['tipo_carroceria'],
        CAPACIDADE_CARGA=dados_veiculo['capacidade_carga'],
        STATUS = "Disponível"#padrão para todo cadastro novo.
    )
    try:
        db.session.add(novo_veiculo)
        db.session.commit()
        return{"mensagem":f"Veículo de placa{novo_veiculo.PLACA} foi cadastrado com sucesso. ID: {novo_veiculo.ID_VEICULO}"} 
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Erro ao cadastrar veículo: {e}")


#CONSULTAR VEÍCULO
def consultar_veiculo(id_veiculo=None, placa=None):
    if id_veiculo:
        return Veiculo.query.get(id_veiculo)
    elif placa:
        return Veiculo.query.filter_by(PLACA=placa).first()
    raise ValueError("Nenhum critério de busca fornecido")
#VERIFICAR A POSSIBILIDADE DE ADICIONAR SOBRE OS STATUS.


#ATUALIZAR VEÍCULO
def atualizar_veiculo(id_veiculo, dados_veiculo):
    veiculo = Veiculo.query.get(id_veiculo)
    if not veiculo:
        raise ValueError("Veículo não encontrado")
    
    campos_permitidos = ['PLACA', 'MARCA', 'MODELO', 'COR', 'ANO_FABRICACAO', 'RENAVAM', 'CHASSI', 'TIPO_CARROCERIA', 'CAPACIDADE_CARGA']
    for campo, valor in dados_veiculo.items():
        if campo in campos_permitidos:
            setattr(veiculo, campo, valor)
    db.session.commit()
    return veiculo


#CANCELAR VEÍCULO(DESATIVAR)
def cancelar_veiculo(id_veiculo, placa):
    """Atualiza o status do veículo para 'Desativado'."""
    veiculo = Veiculo.query.get(id_veiculo, placa)
    if not veiculo:
        raise ValueError("Veículo não encontrado")
    
    if veiculo.STATUS == "Desativado":
        raise ValueError("O veículo já está desativado.")
    
    if veiculo.STATUS != "Disponível":
        raise ValueError("Somente veículos com status 'Disponível' podem ser desativados.")

    
    dados_veiculo = {
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
    print(dados_veiculo)
    # Atualiza o status para 'Desativado'
    veiculo.STATUS = "Desativado"
    db.session.commit()
    return {"mensagem": f"Veículo de ID {id_veiculo} foi desativado com sucesso."}

'''
ATRIBUIR ESSE BLOCO A FUNÇÃO DA TABELA ROTA RESPONSÁVEL POR ATRIBUIR CARRO A ROTA.

if veiculo.STATUS == "Desativado":
    raise ValueError("Veículo desativado não pode ser atribuído a uma rota.")

'''