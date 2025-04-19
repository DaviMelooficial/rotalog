from flask import request, jsonify  
from ..extensions import db
from validate_docbr import CNPJ
from ..models.clientes import Cliente

def cadastrar_cliente(dados):
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
        status="ATIVO"
    )
    
    try:
        db.session.add(novo_cliente)
        db.session.commit()
        return novo_cliente
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao persistir cliente: {str(e)}")
    
def consultar_cliente(cnpj):
    if not cnpj:
        raise ValueError("CNPJ não fornecido")

    cliente = Cliente.query.filter_by(cnpj=cnpj).first()

    if not cliente:
        raise ValueError("Cliente não encontrado")

    return cliente

def listar_clientes():
    return Cliente.query.all()

def atualizar_cliente(cnpj, dados):
    # Busca o cliente
    cliente = Cliente.query.filter_by(cnpj=cnpj).first()
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

def desativar_cliente(cnpj):
    cliente = Cliente.query.filter_by(cnpj=cnpj).first()
    if not cliente:
        raise ValueError("Cliente não encontrado")

    # Verifica se o cliente já está inativo (status False)
    if  cliente.status == "INATIVO":
        raise ValueError("Cliente já está inativo")

    cliente.status ="INATIVO"  # Exclusão lógica (cliente inativo)
    #criar bloco para que ele seja impossibilitado de ser usado em formação de rotas.

    try:
        db.session.commit()  # Persiste as alterações no banco
        return cliente  # Retorna o cliente com as alterações feitas
    except Exception as e:
        db.session.rollback()  # Desfaz as alterações caso ocorra erro
        raise Exception(f"Falha ao desativar cliente: {str(e)}")
