from flask import request, jsonify  
from ..extensions import db
from validate_docbr import CNPJ
from ..models.clientes import Cliente

def cadastrar_cliente(dados):#CRIAR NOVO CLIENTE.
    # Validações
    if not all(key in dados for key in ['cnpj', 'email', 'razao_social']):
        raise ValueError("CNPJ, e-mail e razão social são obrigatórios")
    
    if not CNPJ().validate(dados['cnpj']):
        raise ValueError("CNPJ inválido")
    
    # Verifica duplicata
    if Cliente.query.filter_by(cnpj=dados['cnpj']).first():
        raise ValueError(f"CNPJ {dados['cnpj']} já cadastrado")
    
    # Criação do objeto
    novo_cliente = Cliente(
        cnpj=dados['cnpj'],
        razao_social=dados['razao_social'],
        nome_fantasia=dados.get('nome_fantasia'),
        email=dados['email'],
        telefone=dados['telefone'],
        bairro=dados['bairro'],
        logradouro=dados['logradouro'],
        cidade=dados['cidade'],
        estado=dados['estado'],
        cep=dados['cep'],
        inscricao_estadual=dados.get('inscricao_estadual'),
        inscricao_municipal=dados.get('inscricao_municipal'),
        observacoes=dados.get('observacoes'),
        status=True
    )
    
    try:
        db.session.add(novo_cliente)
        db.session.commit()
        return novo_cliente
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao persistir cliente: {str(e)}")
    
def consultar_cliente(id=None, cnpj=None):#CONSULTAR BANCO DE DADOS PARA VER CLIENTE.

    if not id and not cnpj:
        raise ValueError("Nenhum critério de busca fornecido (ID ou CNPJ)")
    cliente = None
    if id:
        cliente = Cliente.query.get(id)
    elif cnpj:
        cliente = Cliente.query.filter_by(cnpj=cnpj).first()
    if not cliente:
        raise ValueError("Cliente não encontrado")
    return cliente

def atualizar_cliente(id, dados): #ATUALIZAR CLIENTE.
    # Busca o cliente
    cliente = Cliente.query.get(id)
    if not cliente:
        raise ValueError("Cliente não encontrado")

    # Validações específicas (se campos forem fornecidos)
    if 'cnpj' in dados and not CNPJ().validate(dados['cnpj']):
        raise ValueError("CNPJ inválido")

    # Atualiza campos permitidos (exceto ID e campos calculados)
    campos_permitidos = {
        'cnpj', 'razao_social', 'nome_fantasia', 'email',
        'telefone', 'logradouro', 'bairro', 'cidade', 
        'estado', 'cep', 'inscricao_estadual','inscricao_municipal', 'observacoes', 'status'
    }
    
    for campo, valor in dados.items():
        if campo in campos_permitidos:
            setattr(cliente, campo, valor)

    try:
        db.session.commit()
        return cliente
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Falha ao atualizar cliente: {str(e)}")

def deletar_cliente(id):#DELETAR CLIENTE
    cliente = Cliente.query.get(id)
    if not cliente:
        raise ValueError("Cliente não encontrado")

    if not cliente.status:
        raise ValueError("Cliente já está inativo")

    try:
        cliente.status = False  # Exclusão lógica
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Falha ao desativar cliente: {str(e)}")