from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    status = db.Column(db.String(10), nullable=False, default='active')
    name = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=False, nullable=False)
    position = db.Column(db.String(30), nullable=False) # 1 - Operacional, 2 - Supervisão, 3 - Gerência, 4 - Diretoria, 5 - TI
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    reset_token = db.Column(db.String(128), nullable=True)  # Novo campo para o token
    reset_token_expires = db.Column(db.DateTime, nullable=True)  # Nova coluna para expiração do token

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        self.last_password_change = datetime.now()  # Atualiza a data de alteração da senha

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)