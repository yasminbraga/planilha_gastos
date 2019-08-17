from app import db
from datetime import datetime


class BaseModel:
    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=datetime.now)


class Categoria(db.Model, BaseModel):
    __tablename__ = 'categoria'

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)
    titulo = db.Column(db.String(20),nullable=False)
    descricao = db.Column(db.String(100))

    saidas = db.relationship('Saida', cascade='all, delete', backref='saidas', lazy=True)


class Saida(db.Model, BaseModel):
    __tablename__ = 'saida'

    descricao = db.Column(db.String(100))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)
    categoria_id = db.Column(db.Integer,db.ForeignKey('categoria.id'))
    valor = db.Column(db.Float,nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.now)

    categoria = db.relationship('Categoria', backref=db.backref('categoria', cascade='all,delete'), lazy=True)


class Entrada(db.Model, BaseModel):
    __tablename__ = 'entrada'

    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)
    descricao = db.Column(db.String(100))
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.now)


class Movimento(db.Model, BaseModel):
    __tablename__ = 'movimento'

    tipo = db.Column(db.String, nullable=False)

    saida_id = db.Column(db.Integer,db.ForeignKey('saida.id'), nullable=True)
    entrada_id = db.Column(db.Integer,db.ForeignKey('entrada.id'), nullable=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=True)

    saldo = db.Column(db.Float, nullable=False)

    saida = db.relationship('Saida', backref=db.backref('saida', cascade="all,delete"), uselist=False)
    entrada = db.relationship('Entrada', backref=db.backref('entrada',cascade="all,delete"), uselist=False)

    def update(self, saldo):
        self.saldo += saldo
        db.session.commit()


class User(db.Model, BaseModel):
    __tablename__ = 'user'

    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)

    saidas = db.relationship('Saida', cascade='all, delete', backref='user_saidas', lazy=True)
    entradas = db.relationship('Entrada', cascade='all, delete', backref='user_entradas', lazy=True)
    categorias = db.relationship('Categoria', cascade='all, delete', backref='user_categorias', lazy=True)
    movimentos = db.relationship('Movimento', cascade='all, delete', backref='user_movimentos', lazy=True)

    def __init__(self, form):
        self.name = form.name.data
        self.email = form.email.data
        self.username = form.username.data
        self.password = form.password.data
    
    def update_values(self, form):
        self.name = form.name.data
        self.email = form.email.data
        self.username = form.username.data
        self.password = form.password.data
