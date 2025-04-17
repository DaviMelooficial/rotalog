from ..models import Entrega, Cliente
from ..extensions import db
from datetime import datetime

#CADASTRO DE ENTREGA:
def cadastrar_entrega(dados):
    if not Cliente.query.filter_by(cnpj=dados['cnpj_cliente']).first(): #verificação de existencia do cliente.
        raise ValueError("Cliente não encontrado")
    
    nova_entrega = Entrega(
        cnpj_cliente=dados['cnpj_cliente'],
        nota_fiscal=dados['nota_fisca'],
        endereco_endrega=dados['endereco_endrega'],
        volume=dados['volume'],
        data_entrega=datetime.strptime(dados['data_entrega'], '%Y-%m-%d')
    )
    db.session.add(nova_entrega)
    db.session.commit()
    return nova_entrega

#CONSULTA DE ENTREGA:
def consultar_entrega(id_entrega=None, nota_fiscal=None):
    if id_entrega:
        return Entrega.query.get(id_entrega)
    elif nota_fiscal:
        return Entrega.query.filter_by(NOTA_FISCAL=nota_fiscal).first()
    raise ValueError("Nenhum critério de busca fornecido")

#ATUALIZAR CADASTRO:
def atualizar_entrega(id_entrega, dados):#RECEBE OS PARAMETROS AO LADO, ID_ENTREGA PARA INDENTIFICAR E DADOS PARA ATUALIZAR A TABELA DADOS.
    entrega = Entrega.query.get(id_entrega)
    if not entrega:
        raise ValueError("Entrega não encontrada")
    
    campos_permitidos = ['endereco_entrega', 'volume', 'data_entrega', 'rota']
    for campo, valor in dados.items():
        if campo in campos_permitidos:
            setattr(entrega, campo, valor)
    db.session.commit()
    return entrega

# DELETE (Lógico)
def cancelar_entrega(id_entrega):
    """Remove a vinculação com a rota (ROTA=NULL) em vez de apagar."""
    entrega = Entrega.query.get(id_entrega)
    if not entrega:
        raise ValueError("Entrega não encontrada")
    
    entrega.ROTA = None  # Desvincula da rota sem excluir
    db.session.commit()
    return True