from app import app
from flask import render_template, request
from app.models.models import Carteira, Saida, Entrada, Movimento
from app import db


@app.route('/')
def index_dashboard():
    carteira = Carteira.query.get(1)
    ultima_saida = Saida.query.order_by(db.desc(Saida.created_at)).first()
    ultima_entrada = Entrada.query.order_by(db.desc(Entrada.created_at)).first()
    movimentos = Movimento.query.order_by(db.desc(Movimento.created_at)).limit(8).all()
    saida_total = db.session.query(db.func.sum(Saida.valor)).first()[0]    
    
    saidas_categoria = db.session.execute(
        """
        select categoria.titulo, sum(saida.valor)
        from saida
        inner join categoria on categoria.id = saida.categoria_id
        group by saida.categoria_id, categoria.titulo
        """)

    return render_template('dashboard/index.html',
                            carteira=carteira,
                            ultima_saida=ultima_saida,
                            ultima_entrada=ultima_entrada,
                            movimentos=movimentos,
                            saida_total=saida_total,
                            saidas_categoria=saidas_categoria)
