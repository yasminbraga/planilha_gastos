from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models.models import Categoria
from app.controllers.login import login_required


@app.route('/categorias')
@login_required
def index_categorias():
    categorias = Categoria.query.filter(Categoria.user_id == session.get('user_id'))
    return render_template('categorias/index.html', categorias=categorias)

@app.route('/categorias/new', methods=['GET','POST'])
@login_required
def new_categoria():

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        categoria = Categoria(titulo=titulo, descricao=descricao, user_id=session.get('user_id'))
        db.session.add(categoria)
        db.session.commit()
        flash("Categoria criada", "success")
        return redirect(url_for('index_categorias'))
    return render_template('categorias/new.html')

@app.route('/categorias/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_categoria(id):
    categoria = Categoria.query.get(id)
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        categoria.titulo = titulo
        categoria.descricao = descricao
        db.session.commit()
        flash("Categoria editada", "success")
        return redirect(url_for('index_categorias'))
    return render_template('categorias/edit.html',categoria=categoria)


@app.route('/categorias/delete/<int:id>')
@login_required
def delete_categoria(id):
    categoria = Categoria.query.get(id)

    db.session.delete(categoria)
    db.session.commit()
    flash("Categoria excluida", "success")
    return redirect(url_for('index_categorias'))
