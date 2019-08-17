from app import app
from flask import render_template, request, redirect, url_for, flash, session
from app.models.models import Entrada, Movimento
from app import db
from app.controllers.login import login_required


def nova_entrada(entrada, form):
    entrada.valor=form.get('valor')
    entrada.data=form.get('data')
    entrada.descricao=form.get('descricao')
    
    return entrada


@app.route('/entradas')
@login_required
def index_entradas():
    entradas = Entrada.query.all()
    return render_template('entradas/index.html', entradas=entradas)


@app.route('/entradas/new', methods=['GET','POST'])
@login_required
def new_entrada():
    if request.method == 'POST':
        entrada = nova_entrada(Entrada(), request.form)
        db.session.add(entrada)
        db.session.commit()
        movimento = Movimento(tipo='entrada', entrada_id=entrada.id, user_id=session.get('user_id'), saldo=entrada.valor)
        db.session.add(movimento)
        db.session.commit()
        flash("Entrada criada", "success")
        return redirect(url_for('index_entradas')) 
    return render_template('entradas/new.html')


@app.route('/entradas/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_entrada(id):
    entrada = Entrada.query.get(id)
    if request.method == 'POST':
        entrada = nova_entrada(entrada, request.form)
        db.session.add(entrada)
        db.session.commit()
        movimento.query.filter(Movimento.entrada_id == entrada.id).first().update(float(entrada.valor))        
        flash("Entrada editada", "success")
        return redirect(url_for('index_entradas')) 
    return render_template('entradas/new.html', entrada=entrada)


@app.route('/entradas/delete/<int:id>')
@login_required
def delete_entrada(id):
    entrada = Entrada.query.get(id)
    db.session.delete(entrada)
    db.session.commit()
    flash("Entrada excluida", "success")
    return redirect(url_for('index_entradas'))
