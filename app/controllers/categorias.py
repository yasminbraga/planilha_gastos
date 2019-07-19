from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.models import Categoria

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

        categorias = Categoria.query.all()

        return redirect(url_for('index_categorias', categorias=categorias))

    return render_template('categorias/new.html')