from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.models import Categoria, Saida, Carteira, Movimento
from datetime import datetime


def nova_saida(saida, form):
    saida.valor=form.get('valor')
    saida.data=form.get('data')
    saida.categoria_id=form.get('categoria_id')
    saida.descricao=form.get('descricao')
    
    return saida


@app.route('/saidas')
def index_saidas():
    saidas = Saida.query.all()
    return render_template('saidas/index.html',saidas=saidas)


@app.route('/saidas/new', methods=['GET','POST'])
def new_saidas():
    categorias = Categoria.query.all()
    if request.method == 'POST':
        saida = nova_saida(Saida(),request.form)
        Carteira.query.first().update(-float(saida.valor))
        db.session.add(saida)
        db.session.commit()
        movimento = Movimento(tipo='saida', saida_id=saida.id)
        db.session.add(movimento)
        db.session.commit()
        flash("Saida criada", "success")
        return redirect(url_for('index_saidas'))
    return render_template('saidas/new.html', categorias=categorias)

@app.route('/saidas/edit/<int:id>', methods=['GET','POST'])
def edit_saida(id):

    categorias = Categoria.query.all()
    saida = Saida.query.get(id)

    if request.method == 'POST':
        saida = nova_saida(saida, request.form)
        Carteira.query.first().update(-float(saida.valor))
        db.session.add(saida)
        db.session.commit()
        flash("Saida editada", "success")
        return redirect(url_for('index_saidas'))
    
    return render_template('saidas/edit.html', saida=saida, categorias=categorias)

@app.route('/saidas/delete/<int:id>')
def delete_saida(id):
    saida = Saida.query.get(id)
    Carteira.query.first().update(float(saida.valor))
    db.session.delete(saida)
    db.session.commit()
    flash("Saida deletada", "success")
    return redirect(url_for('index_saidas'))
