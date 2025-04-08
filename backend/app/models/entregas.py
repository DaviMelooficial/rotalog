from datetime import datetime
from ..extensions import db
from sqlalchemy import ForeignKey


class Entrega(db.Model):
    __tablename__ = 'entregas'
    
    id_entrega = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj_cliente = db.Column(db.String(14), ForeignKey('clientes.cnpj'), nullable=False)  # Relacionamento
    nota_fiscal = db.Column(db.String(50), unique=True, nullable=False),
    endereco_entrega = db.Column(db.String(300), nullable=False),
    volume = db.Column(db.Float, nullable=False),
    data_entrega = db.Column(db.DateTime, default=datetime.now, nullable=False),
    rota = db.Column(db.Integer, ForeignKey('rotas.ID_ROTA'), nullable=True)  # Chave estrangeira (se a tabela Rota existir)
                    
def __repr__(self):
        return f'<Entrega {self.NOTA_FISCAL} - Cliente: {self.CNPJ_CLIENTE}>'  

