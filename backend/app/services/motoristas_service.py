from flask import request, jsonify  
from ..extensions import db
from validate_docbr import CPF
from ..models.motoristas import Motorista


#CADASTRAR MOTORISTA:
def cadastrar_motorista(dados):

    if not all(key in dados for key in ['nome_motorista', 'cpf', 'cnh']):
        raise ValueError("Nome completo, CPF e CNH são obrigatórios")
    
    cpf_validator = CPF()
    if not cpf_validator.validate(dados['cpf']):
        raise ValueError("CPF inválido")
    

    if Motorista.query.filter_by(cpf=dados['cpf'], cnh=dados['cnh']).first():
        raise ValueError("Motorista já cadastrado")
    
    # Cria o objeto Motorista
    novo_motorista = Motorista(
        nome_motorista=dados['nome_motorista'],
        cpf=dados['cpf'],
        cnh=dados['cnh'],
        classificacao=dados.get('classificacao'),
        telefone=dados.get('telefone')
    )

    # Salva no banco de dados
    try:
        db.session.add(novo_motorista)
        db.session.commit()
        return {"mensagem": f"Motorista {novo_motorista.nome_motorista} cadastrado com sucesso. ID: {novo_motorista.id_motorista}"}
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao cadastrar motorista: {str(e)}")

#CONSULTAR DE MOTORISTA:
def consultar_motorista(id_motorista=None, cnh=None):
    if id_motorista:
        return Motorista.query.get(id_motorista)
    elif cnh:
        return Motorista.query.filter_by(CNH=cnh).first()
    raise ValueError("Nenhum critério de busca fornecido")

def listar_motoristas():
    return Motorista.query.all()

#ATUALIZAR CADASTRO DE MOTORISTA:
def atualizar_motorista(id_motorista, dados):
    motorista = Motorista.query.get(id_motorista)
    if not motorista:
        raise ValueError("Motorista não encontrado")
    
    campos_permitidos = ['nome_motorista', 'CPF', 'CNH', 'classificacao', 'Telefone']
    for campo, valor in dados.items():
        if campo in campos_permitidos:
            setattr(motorista, campo, valor)
    db.session.commit()
    return motorista

#CANCELAR MOTORISTA:
def cancelar_motorista(id_motorista):
    """Remove o motorista da tabela sem excluir."""
    motorista = Motorista.query.get(id_motorista)
    if not motorista:
        raise ValueError("Motorista não encontrado")
    
    db.session.delete(motorista)  # Remove o motorista da sessão
    db.session.commit()
    return True