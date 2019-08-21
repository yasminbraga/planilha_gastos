from flask import render_template, request, url_for, redirect, flash, session
from app import app, db
from app.models.models import User
from app.forms.user import UserForm, EditUserForm
from app.controllers.login import login_required


@app.route('/users')
@login_required
def index_users():
    users = User.query.all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def new_users():
    if session.get('logged_in'): return redirect(url_for('index_dashboard'))
    form = UserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user_exists = User.query.filter(User.name == form.name.data).first()
            if not user_exists:
                email_exists = User.query.filter(User.email == form.email.data).first()
                if not email_exists:
                    user = User(form)
                    db.session.add(user)
                    db.session.commit()
                    flash('Usuário registrado', 'success')
                    return redirect(url_for('index_users'))
                else:
                    flash('Email já existe', 'danger')
            else:
                flash('Usuario já existe', 'danger')
        else:
            flash('Erro ao registrar usuário', 'danger')
    return render_template('users/new.html', form=form)


@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_users(id):
    user = User.query.get(id)
    form = UserForm(request.form, obj=user)
    if request.method == 'POST':
        if form.validate:
            user_exists = User.query.filter(User.name == form.name.data).first()
            if not user_exists or user_exists.username == user.username:
                email_exists = User.query.filter(User.email == form.email.data).first()
                if not email_exists or email_exists.email == user.email:
                    form.populate_obj(user)
                    db.session.add(user)
                    db.session.commit()
                    flash('Usuário editado', 'success')
                    return redirect(url_for('index_users'))
                else:
                    flash('Email já existe', 'danger')
            else:
                flash('Usuario já existe', 'danger')
        else:
            flash('Erro ao registrar usuário', 'danger')
    return render_template('users/edit.html', form=form, editing=True)


@app.route('/users/delete/<int:id>')
@login_required
def delete_users(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário deletado', 'success')
    return redirect(url_for('index_users'))

