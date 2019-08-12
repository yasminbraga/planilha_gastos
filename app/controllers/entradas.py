from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models.models import Carteira, Entrada, Movimento
from app import db


def nova_entrada(entrada, form):
    entrada.valor=form.get('valor')
    entrada.data=form.get('data')
    entrada.descricao=form.get('descricao')
    
    return entrada


@app.route('/entradas')
def index_entradas():
    entradas = Entrada.query.all()
    return render_template('entradas/index.html', entradas=entradas)


@app.route('/entradas/new', methods=['GET','POST'])
def new_entrada():
    if request.method == 'POST':
        entrada = nova_entrada(Entrada(), request.form)
        Carteira.query.first().update(float(entrada.valor))
        db.session.add(entrada)
        db.session.commit()
        movimento = Movimento(tipo='entrada', entrada_id=entrada.id)
        db.session.add(movimento)
        db.session.commit()
        flash("Entrada criada", "success")
        return redirect(url_for('index_entradas')) 
    return render_template('entradas/new.html')


@app.route('/entradas/edit/<int:id>', methods=['GET','POST'])
def edit_entrada(id):
    entrada = Entrada.query.get(id)
    if request.method == 'POST':
        entrada = nova_entrada(entrada, request.form)
        Carteira.query.first().update(float(entrada.valor))
        db.session.add(entrada)
        db.session.commit()
        flash("Entrada editada", "success")
        return redirect(url_for('index_entradas')) 
    return render_template('entradas/new.html', entrada=entrada)


@app.route('/entradas/delete/<int:id>')
def delete_entrada(id):
    entrada = Entrada.query.get(id)
    Carteira.query.first().update(-float(entrada.valor))
    db.session.delete(entrada)
    db.session.commit()
    flash("Entrada excluida", "success")
    return redirect(url_for('index_entradas'))
