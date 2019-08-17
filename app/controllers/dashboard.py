from app import app
from flask import render_template, request, session
from app.models.models import Saida, Entrada, Movimento
from app import db
from app.controllers.login import login_required

@app.route('/dashboard')
@login_required
def index_dashboard():
    saldo_total = db.session.query(db.func.sum(Movimento.saldo)).filter(Movimento.user_id == session.get('user_id')).first()[0] or 0.0
    ultima_saida = Saida.query.order_by(db.desc(Saida.created_at)).filter(Movimento.user_id == session.get('user_id')).first()
    ultima_entrada = Entrada.query.order_by(db.desc(Entrada.created_at)).filter(Movimento.user_id == session.get('user_id')).first()
    movimentos = Movimento.query.order_by(db.desc(Movimento.created_at)).filter(Movimento.user_id == session.get('user_id')).limit(8).all()
    saida_total = db.session.query(db.func.sum(Saida.valor)).filter(Movimento.user_id == session.get('user_id')).first()[0]    
    
    saidas_categoria = db.session.execute(
        f"""
        select categoria.titulo, sum(saida.valor)
        from saida
        inner join categoria on categoria.id = saida.categoria_id
        where categoria.user_id = {session.get('user_id')}
        group by saida.categoria_id, categoria.titulo
        """)

    ctx = {
        'saldo_total':saldo_total,
        'ultima_saida':ultima_saida,
        'ultima_entrada':ultima_entrada,
        'movimentos':movimentos,
        'saida_total':saida_total,
        'saidas_categoria':saidas_categoria

    }

    return render_template('dashboard/index.html', **ctx)
