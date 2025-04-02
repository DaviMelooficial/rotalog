from ..extensions import db
from sqlalchemy import ForeignKey


class Rota(db.Model):
    __tablename__ = 'rotas'
    
    id_rota = db.Column(db.Integer, primary_key=True, autoincrement=True)
    motorista = db.Column(db.String(100), nullable=False)
    
    entregas = db.relationship('Entrega', backref='rota', lazy=True)

    def __repr__(self):
        return f'<Rota {self.id_rota} - Motorista: {self.motorista}>'