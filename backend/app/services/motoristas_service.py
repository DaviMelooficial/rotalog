from ..extensions import db
from ..models.motoristas import Motorista

#CADASTRAR MOTORISTA:
def cadastrar_motorista(dados):
    if Motorista.query.filter_by(nome_motorista=dados['nome_motorista'], CPF=dados['cpf'], CNH=dados['cnh']).first():
        raise ValueError("Motorista já cadastrado")
    

    novo_motorista = Motorista(
        nome_motorista=dados['nome_motorista'],
        CPF=dados['cpf'],
        CNH=dados['cnh'],
        classificacao=dados['classificacao'],
        Telefone=dados['telefone']
    )
    db.session.add(novo_motorista)
    db.session.commit()
    return novo_motorista


#CONSULTAR DE MOTORISTA:
def consultar_motorista(id_motorista=None, cnh=None):
    if id_motorista:
        return Motorista.query.get(id_motorista)
    elif cnh:
        return Motorista.query.filter_by(CNH=cnh).first()
    raise ValueError("Nenhum critério de busca fornecido")

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