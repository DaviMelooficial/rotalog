from ..extensions import db

class Motorista(db.Model):
    __tablename__ = 'motoristas'

    id_motorista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_motorista = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False, index=True)
    cnh = db.Column(db.String(20), unique=True, nullable=False, index=True)
    classificacao = db.Column(db.String(20), nullable=False)  # Ex: Categoria A, B, C, D, E
    telefone = db.Column(db.String(20), nullable=False)
