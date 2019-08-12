from app import db
from datetime import datetime


class BaseModel:
    id = db.Column(db.Integer,primary_key=True)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=datetime.now)


class Categoria(db.Model, BaseModel):
    __tablename__ = 'categoria'

    titulo = db.Column(db.String(20),nullable=False)
    descricao = db.Column(db.String(100))

    saidas = db.relationship('Saida', cascade='all, delete', backref='saidas', lazy=True)



class Carteira(db.Model, BaseModel):
    __tablename__ = 'carteira'
    
    saldo = db.Column(db.Float,nullable=False)

    def update(self, saldo):
        self.saldo += saldo
        db.session.commit()


class Saida(db.Model, BaseModel):
    __tablename__ = 'saida'

    descricao = db.Column(db.String(100))
    categoria_id = db.Column(db.Integer,db.ForeignKey('categoria.id'))
    valor = db.Column(db.Float,nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.now)

    categoria = db.relationship('Categoria', backref=db.backref('categoria', cascade='all,delete'), lazy=True)


class Entrada(db.Model, BaseModel):
    __tablename__ = 'entrada'

    descricao = db.Column(db.String(100))
    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.now)


class Movimento(db.Model, BaseModel):
    __tablename__ = 'movimento'

    tipo = db.Column(db.String, nullable=False)

    saida_id = db.Column(db.Integer,db.ForeignKey('saida.id'), nullable=True)
    entrada_id = db.Column(db.Integer,db.ForeignKey('entrada.id'), nullable=True)

    saida = db.relationship('Saida', backref=db.backref('saida', cascade="all,delete"), uselist=False)
    entrada = db.relationship('Entrada', backref=db.backref('entrada',cascade="all,delete"), uselist=False)


class Saldo(db.Model, BaseModel):
    __tablename__ = 'saldo'

    valor = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime(timezone=True), default=datetime.now)
    movimento_id = db.Column(db.Integer,db.ForeignKey('movimento.id'))
    movimento = db.relationship('Movimento', backref=db.backref('movimento', uselist=False))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, nullable=False)