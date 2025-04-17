from ..extensions import db

class Motorista(db.Model):
    __tablename__ = 'motoristas'

    Id_motorista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_motorista = db.Column(db.String(255), nullable=False)
    CPF = db.Column(db.String(11), unique=True, nullable=False, index=True)
    CNH = db.Column(db.String(20), unique=True, nullable=False, index=True)
    classificacao = db.Column(db.String(20), nullable=False)  # Ex: Categoria A, B, C, D, E
    Telefone = db.Column(db.String(20), nullable=False)


