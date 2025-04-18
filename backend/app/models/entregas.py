from datetime import datetime
from ..extensions import db
from ..models.clientes import Cliente


class Entrega(db.Model):
    __tablename__ = 'entregas'
    
    id_entrega = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj_cliente = db.Column(db.String(14), db.ForeignKey('clientes.cnpj'), nullable=False)  # Relacionamento
    nota_fiscal = db.Column(db.String(50), unique=True, nullable=False)
    logradouro_entrega = db.Column(db.String(300), nullable=False)
    bairro_entrega = db.Column(db.String(50), nullable=False)
    cidade_entrega = db.Column(db.String(50), nullable=False)
    estado_entrega = db.Column(db.String(2), nullable=False)
    cep_entrega = db.Column(db.String(8), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    data_entrega = db.Column(db.DateTime, default=datetime.now, nullable=False)
    status_entrega = db.Column(db.String(20), default='Pendente', nullable=False)  # Status da entrega (Pendente, Entregue, Cancelada)
    # ID_ROTA = db.Column(db.Integer, db.ForeignKey('rotas.ID_ROTA'), nullable=True)  # Chave estrangeira (se a tabela Rota existir)
                    
    def __repr__(self):
        return f'<Entrega {self.nota_fiscal} - Cliente: {self.cnpj_cliente}>'
