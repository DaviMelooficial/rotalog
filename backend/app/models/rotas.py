from ..extensions import db
from datetime import datetime

class Rota(db.Model):
    __tablename__ = 'rotas'
    
    ID_ROTA = db.Column(db.Integer, primary_key=True, autoincrement=True)
    DATA_CRIACAO = db.Column(db.DateTime, default=datetime.now, nullable=False)
    DESTINO = db.Column(db.String(255), nullable=False)  # Ex: São Paulo, Rio de Janeiro, etc.  
    ENTREGAS = db.Column(db.String(255), nullable=False)  # Ex: Entrega 1, Entrega 2, etc.
    #PREVISAO_ENTREGAS = db.Column(db.Date, nullable=False)  # Data prevista para as entregas
    STATUS = db.Column(db.String(20), nullable=False, default='planejada')  # Ex: Em planejamento, planejada, em_transporte, concluída
    MOTORISTA = db.Column(db.Integer, db.ForeignKey('motoristas.nome_motorista'), nullable=True)  # Se houver tabela Motorista
    VEICULO_ID = db.Column(db.Integer, db.ForeignKey('veiculos.ID_VEICULO'), nullable=True)  # Se houver tabela Veículo
    OBSERVACOES = db.Column(db.Text)


    #A rota precisa ser planejada de acordo com a região das entregas, e identificada por algum fator além do ID.
    #Planejamento de rota deve ser alinhado junto com equipe de gerencia e logística.
    #Relacionamento com entregas (uma rota tem muitas entregas)
    entregas = db.relationship('Entrega', backref='rota_vinculada', lazy=True)

   



    



