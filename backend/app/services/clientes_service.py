from flask import request, jsonify  
from ..extensions import db  
from ..models import cliente
from validate_docbr import CNPJ, CEP  
from app import app

from ..models import Cliente
from validate_docbr import CNPJ, CEP
from ..extensions import db

def cadastrar_cliente(dados):#CRIAR NOVO CLIENTE.
    """
    Função pura para cadastro de cliente (sem dependências HTTP).
    Retorna o objeto Cliente em caso de sucesso ou levanta erros específicos.
    
    Args:
        dados (dict): Dicionário com:
            - cnpj (str)
            - razao_social (str)
            - email (str)
            - telefone (str)
            - cep (str)
            - ... (outros campos do modelo Cliente)
    
    Returns:
        Cliente: Objeto do cliente cadastrado
    
    Raises:
        ValueError: Em caso de dados inválidos ou duplicados
        Exception: Erros inesperados no banco
    """
    # Validações
    if not all(key in dados for key in ['cnpj', 'email', 'razao_social']):
        raise ValueError("CNPJ, e-mail e razão social são obrigatórios")
    
    if not CNPJ().validate(dados['cnpj']):
        raise ValueError("CNPJ inválido")
    
    if not CEP().validate(dados['cep']):
        raise ValueError("CEP inválido")
    
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
        logradouro=dados['logradouro'],
        bairro=dados['bairro'],
        cidade=dados['cidade'],
        estado=dados['estado'],
        cep=dados['cep'],
        inscricao_estadual=dados.get('inscricao_estadual'),
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
    """
    Consulta cliente por ID ou CNPJ (função pura, sem dependências HTTP).
    
    Args:
        id (int, optional): ID do cliente. Defaults to None.
        cnpj (str, optional): CNPJ do cliente. Defaults to None.
    
    Returns:
        Cliente: Objeto do cliente encontrado
    
    Raises:
        ValueError: Se nenhum parâmetro for fornecido ou cliente não existir
    """
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



