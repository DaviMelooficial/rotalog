from ..extensions import db
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy.sql import func
from validate_docbr import CNPJ


class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False, index=True)
    razao_social = db.Column(db.String(255), nullable=False)
    nome_fantasia = db.Column(db.String(255))
    email = db.Column(db.String(100), nullable=False, unique=True)
    telefone = db.Column(db.String(20), nullable=False)
    logradouro = db.Column(db.String(300), nullable=False)
    bairro = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    inscricao_estadual = db.Column(db.String(20))
    inscricao_municipal = db.Column(db.String(20))
    data_atualizacao = db.Column(db.DateTime, onupdate=func.now())
    status = db.Column(db.String(15), default=True)#ATIVO OU INATIVO
    observacoes = db.Column(db.Text)

    # Validação de CNPJ
    @validates('cnpj')
    def validate_cnpj(self, key, cnpj):
        cnpj_limpo = cnpj.replace('.', '').replace('/', '').replace('-', '')
        if not CNPJ().validate(cnpj_limpo):
            raise ValueError("CNPJ inválido")
        return cnpj_limpo  # Salva sem formatação

    def __repr__(self):
        return f'<Cliente {self.cnpj} - {self.razao_social}>'
    
    #DEVEMOS COLOCAR UMA FUNÇÃO PARA VALIDAÇÃO DE CEP?