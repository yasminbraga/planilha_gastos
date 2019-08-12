from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models.models import Categoria, Carteira

@app.route('/categorias')
def index_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias/index.html', categorias=categorias)

@app.route('/categorias/new', methods=['GET','POST'])
def new_categoria():

    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        categoria = Categoria(titulo=titulo, descricao=descricao)
        db.session.add(categoria)
        db.session.commit()
        flash("Categoria criada", "success")
        return redirect(url_for('index_categorias'))
    return render_template('categorias/new.html')

@app.route('/categorias/edit/<int:id>', methods=['GET','POST'])
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
def delete_categoria(id):
    categoria = Categoria.query.get(id)
    for saida in categoria.saidas:
        Carteira.query.first().update(float(saida.valor))

    db.session.delete(categoria)
    db.session.commit()
    flash("Categoria excluida", "success")
    return redirect(url_for('index_categorias'))
