from ..models.entregas import Entrega
from ..models.clientes import Cliente
from ..extensions import db
from datetime import datetime

#CADASTRO DE ENTREGA:
def cadastrar_entrega(dados):
    
    if not Cliente.query.filter_by(cnpj=dados['cnpj_cliente']).first():
        raise ValueError("Cliente não encontrado")
    
    if Entrega.query.filter_by(nota_fiscal=dados['nota_fiscal']).first():
        raise ValueError(f"Nota fiscal {dados['nota_fiscal']} já cadastrada")
    
    nova_entrega = Entrega(
        cnpj_cliente=dados['cnpj_cliente'],
        nota_fiscal=dados['nota_fiscal'],
        logradouro_entrega=dados['logradouro_entrega'],
        bairro_entrega=dados['bairro_entrega'],
        cidade_entrega=dados['cidade_entrega'],
        estado_entrega=dados['estado_entrega'],
        cep_entrega=dados['cep_entrega'],
        volume=dados['volume'],
        data_entrega=datetime.strptime(dados['data_entrega'], '%Y-%m-%d')
    )
    db.session.add(nova_entrega)
    db.session.commit()
    return nova_entrega

#CONSULTA DE ENTREGA:
def consultar_entrega(nota_fiscal):
    if not nota_fiscal:
        raise ValueError("Nota fiscal não fornecida")
    
    # Consulta pelo número da nota fiscal
    entrega = Entrega.query.filter_by(nota_fiscal=nota_fiscal).first()
    if not entrega:
        raise ValueError("Entrega não encontrada para a nota fiscal fornecida")
    
    return entrega

#ATUALIZAR CADASTRO:
def atualizar_entrega(nota_fiscal, dados):
    entrega = Entrega.query.filter_by(nota_fiscal=nota_fiscal).first()
    if not entrega:
        raise ValueError("Entrega não encontrada para NF fornecida")
    
    campos_permitidos = [
        'logradouro_entrega',
        'bairro_entrega',
        'cidade_entrega',
        'estado_entrega',
        'cep_entrega',
        'volume',
        'data_entrega',
        ]
    for campo, valor in dados.items():
        if campo in campos_permitidos:
            if campo == 'data_entrega' and isinstance(valor, str):
                valor = datetime.strptime(valor, '%Y-%m-%d')
            setattr(entrega, campo, valor)
    db.session.commit()
    return entrega

# DELETE (Lógico)
def cancelar_entrega(nota_fiscal):
    """Cancela a entrega alterando o status para 'Cancelada'."""
    entrega = Entrega.query.filter_by(nota_fiscal=nota_fiscal).first()
    if not entrega:
        raise ValueError("Entrega não encontrada para a nota fiscal fornecida")
    
    # Verifica se a entrega já está cancelada
    if entrega.status_entrega == "CANCELADA":
        raise ValueError("A entrega já está cancelada")
    
    # Atualiza o status para "Cancelada"
    entrega.status_entrega = "Cancelada"
    
    try:
        db.session.commit()
        return entrega
    except Exception as e:
        db.session.rollback()
        raise Exception(f"Erro ao cancelar entrega: {str(e)}")