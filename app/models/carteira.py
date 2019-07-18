from app import db
from datetime import datetime


class Carteira(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    saldo = db.Column(db.Float,nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),default=datetime.now)
    updated_at = db.Column(db.DateTime(timezone=True),onupdate=datetime.now)
