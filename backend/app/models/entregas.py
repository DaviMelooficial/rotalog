from ..extensions import db
from sqlalchemy.orm import validates
from sqlalchemy import ForeignKey
from datetime import datetime
from validate_docbr import CNPJ


class Entrega(db.Model):
    __tablename__ = 'entregas'
    
    # Colunas principais
    id_entrega = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nota_fiscal = db.Column(db.String(50), unique=True, nullable=False)
    endereco_entrega = db.Column(db.String(255), nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    data_entrega = db.Column(db.Date, nullable=False)

    # Relacionamento com a tabela Cliente (chave estrangeira)
    cnpj_cliente = db.Column(db.String(14), ForeignKey('clientes.cnpj'), nullable=False)
    cliente = db.relationship('Cliente', backref='entregas')  # Acesso bidirecional
    razao_social = db.Column(db.String(255), nullable=False)
    id_rota = db.Column(db.Integer, ForeignKey('rotas.id_rota'), nullable=True) #coluna de associação com a tabela rota.
