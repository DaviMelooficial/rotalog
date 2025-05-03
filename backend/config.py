import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'PAPIRO_INSANO')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///routes.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'SELVA')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    # Configurações de Email
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'rotalog00@gmail.com'
    MAIL_PASSWORD = 'homj mabg ljet bstk'
    MAIL_DEFAULT_SENDER = ('Rotalog System', 'rotalog00@gmail.com')
    MAIL_MAX_EMAILS = 100
    MAIL_ASCII_ATTACHMENTS = False
    MAIL_SUPPRESS_SEND = False
    MAIL_DEBUG = True  # Defina como False em produção

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}