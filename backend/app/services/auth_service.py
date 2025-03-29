from ..models.user import User
from ..extensions import db

class AuthService:
    @staticmethod
    def create_user(username, cpf, password):
        if User.query.filter_by(username=username).first():
            return None, 'Username already exists'
        if User.query.filter_by(cpf=cpf).first():
            return None, 'cpf already exists'
        
        new_user = User(username=username, cpf=cpf)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        return new_user, None

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return None, 'Invalid credentials'
        return user, None