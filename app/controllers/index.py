from app import app
from flask import render_template, request
from app.models.carteira import Carteira
from app import db


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        saldo = request.form.get('saldo')
        db.session.query(Carteira).update({Carteira.saldo: saldo})
        db.session.commit()
    carteira = Carteira.query.get(1)
    return render_template('index/index.html',carteira=carteira)
