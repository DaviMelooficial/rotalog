from ..models.user import User
from ..extensions import db
from flask import request, jsonify, url_for
from flask_mail import Message
from ..extensions import mail
import random, string, secrets

class AuthService:
    @staticmethod
    def create_user(name, cpf, email, position, username, password):    

        if User.query.filter_by(username=username).first():
            return None, 'Username já existe'
        
        if User.query.filter_by(cpf=cpf).first():
            return None, 'CPF já existe'

        if User.query.filter_by(email=email).first():
            return None, 'E-mail já existe'

        

        new_user = User(
            name=name,
            cpf=cpf,
            email=email,
            position=position,
            username=username,   
        )
        
        new_user.set_password(password)

        # Salva o novo usuário no banco de dados
        try:
            db.session.add(new_user)
            db.session.commit()
            AuthService.send_email_password(email, password, name, username)
            return new_user, None
        except Exception as e:
            db.session.rollback()
            return None, f"Erro ao cadastrar usuário: {str(e)}"
        
    @staticmethod
    def generate_password(size=8):
        caracteres = string.ascii_letters + string.digits  # Letras maiúsculas, minúsculas e números
        return ''.join(random.choice(caracteres) for _ in range(size))

    @staticmethod
    def send_email_password(email, password, name, username):
        try:
            msg = Message(
                subject="Bem Vindo ao Rotalog",
                sender=("Rotalog System", "noreply@rotalog.com"),
                recipients=[email],
                body=f"Olá {name} seu login foi criado com sucesso \n \nAqui estão suas credenciais: \nUsuário: {username} \nSenha: {password}\n \n Por favor, altere sua senha após primeiro acesso.",
                html=f"""
                <html>
                    <body>
                        <h2>Bem-vindo ao Rotalog!</h2>
                        <p>Olá {name},</p>
                        <p>Seu login foi criado com sucesso.</p>
                        <h3>Suas credenciais de acesso:</h3>
                        <p><strong>Usuário:</strong> {username}</p>
                        <p><strong>Senha:</strong> {password}</p>
                        <p style="color: red;"><strong>Importante:</strong> Por favor, altere sua senha após o primeiro acesso.</p>
                        <br>
                        <p>Atenciosamente,<br>Equipe Rotalog</p>
                    </body>
                </html>
                """
            )
            # Adiciona headers importantes
            msg.extra_headers = {
                "List-Unsubscribe": f"<mailto:unsubscribe@rotalog.com?subject=unsubscribe>",
                "Precedence": "bulk"
            }
            mail.send(msg)
        except Exception as e:
            print(f"Erro ao enviar e-mail: {str(e)}")

    @staticmethod
    def authenticate_user(username, password):
        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return None, 'Invalid credentials'
        return user, None

    @staticmethod
    def consult_user(cpf):
        if not cpf:
            raise ValueError("CPF não fornecido")

        cliente = User.query.filter_by(cpf=cpf).first()

        if not cliente:
            raise ValueError("Cliente não encontrado")

        return cliente
    
    @staticmethod
    def list_users():
        return User.query.all()
    
    @staticmethod
    def update_user(cpf, dados):

        user = User.query.filter_by(cpf=cpf).first()
        if not user:
            raise ValueError("Cliente não encontrado")

        allowed_keys = ['name','cpf', 'email', 'position']          

        # Atualiza os dados do cliente
        for key, value in dados.items():
            if key in allowed_keys:
                setattr(user, key, value)

        try:
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao atualizar usuário: {str(e)}")
    
    @staticmethod
    def disable_user(cpf):

        user = User.query.filter_by(cpf=cpf).first()
        if not user:
            raise ValueError("usuário não encontrado")
        
        if user.status == 'INACTIVE':
            raise ValueError("usuário já está inativo")
        
        user.status = 'INACTIVE'

        try:
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao deletar cliente: {str(e)}")
        
    @staticmethod
    def forgot_password(email):
        user = User.query.filter_by(email=email).first()
        if not user:
            raise ValueError("Email não encontrado")

        # Gera nova senha aleatória
        new_password = AuthService.generate_password()
        
        # Atualiza a senha do usuário
        user.set_password(new_password)

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise Exception(f"Erro ao atualizar senha: {str(e)}")

        try:
            msg = Message(
                subject="Nova Senha - Rotalog",
                sender=("Rotalog System", "rotalog00@gmail.com"),
                recipients=[email],
                body=f"""Olá {user.name},

Conforme solicitado, sua senha foi redefinida.
Sua nova senha é: {new_password}

Por favor, altere esta senha após seu próximo login por motivos de segurança.

Atenciosamente,
Equipe Rotalog""",
                html=f"""
                <html>
                    <body>
                        <h2>Nova Senha - Rotalog</h2>
                        <p>Olá {user.name},</p>
                        <p>Conforme solicitado, sua senha foi redefinida.</p>
                        <p><strong>Sua nova senha é:</strong> {new_password}</p>
                        <p style="color: red;"><strong>Importante:</strong> Por favor, altere esta senha após seu próximo login por motivos de segurança.</p>
                        <br>
                        <p>Atenciosamente,<br>Equipe Rotalog</p>
                    </body>
                </html>
                """
            )
            # Adiciona headers importantes
            msg.extra_headers = {
                "List-Unsubscribe": f"<mailto:unsubscribe@rotalog.com?subject=unsubscribe>",
                "Precedence": "bulk"
            }
            mail.send(msg)
            return True
        except Exception as e:
            raise Exception(f"Erro ao enviar e-mail: {str(e)}")
