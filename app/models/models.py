from app import db
from datetime import datetime


class BaseModel:
    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True),default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True),onupdate=datetime.now)


class Categoria(db.Model, BaseModel):
    __tablename__ = 'categoria'

    titulo = db.Column(db.String(20),nullable=False)
    descricao = db.Column(db.String(100))


class Carteira(db.Model, BaseModel):
    __tablename__ = 'carteira'
    
    saldo = db.Column(db.Float,nullable=False)
   