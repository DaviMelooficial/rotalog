from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask import Flask
from flask import Blueprint
from datetime import datetime


db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()