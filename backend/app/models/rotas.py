from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class Rota(db.Model):
    __tablename__ = 'rotas'
    
    id_rota = db.Column(db.Integer, primary_key=True, autoincrement=True)
    motorista = db.Column(db.String(100), nullable=False)
    
    entregas = db.relationship('Entrega', backref='rota', lazy=True)

    def __repr__(self):
        return f'<Rota {self.id_rota} - Motorista: {self.motorista}>'