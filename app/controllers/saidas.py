from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models.models import Categoria, Saida, Movimento
from datetime import datetime
from app.controllers.login import login_required



def nova_saida(saida, form):
    saida.valor=form.get('valor')
    saida.data=form.get('data')
    saida.categoria_id=form.get('categoria_id')
    saida.descricao=form.get('descricao')
    
    return saida


@app.route('/saidas')
@login_required
def index_saidas():
    saidas = Saida.query.all()
    return render_template('saidas/index.html',saidas=saidas)


@app.route('/saidas/new', methods=['GET','POST'])
@login_required
def new_saidas():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        saida = nova_saida(Saida(user_id=session.get("user_id")),request.form)
        db.session.add(saida)
        db.session.commit()
        movimento = Movimento(tipo='saida', saida_id=saida.id,user_id=session.get('user_id'), saldo=-float(saida.valor))
        db.session.add(movimento)
        db.session.commit()
        flash("Saida criada", "success")
        return redirect(url_for('index_saidas'))
    return render_template('saidas/new.html', categorias=categorias)

@app.route('/saidas/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_saida(id):

    categorias = Categoria.query.all()
    saida = Saida.query.get(id)

    if request.method == 'POST':
        saida = nova_saida(saida, request.form)
        db.session.add(saida)
        db.session.commit()
        movimento.query.filter(Movimento.saida_id == saida.id).first().update(-float(saida.valor))
        flash("Saida editada", "success")
        return redirect(url_for('index_saidas'))
    
    return render_template('saidas/edit.html', saida=saida, categorias=categorias)

@app.route('/saidas/delete/<int:id>')
@login_required
def delete_saida(id):
    saida = Saida.query.get(id)
    db.session.delete(saida)
    db.session.commit()
    flash("Saida deletada", "success")
    return redirect(url_for('index_saidas'))
