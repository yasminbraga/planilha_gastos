from flask import render_template, request, url_for, redirect, flash, session
from app import app, db
from app.models.models import User
from app.forms.login import LoginForm
from functools import wraps



def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not session.get('logged_in'):
            flash('Login required', 'danger')
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            user = User.query.filter(User.username == form.username.data).first()
            if user:
                if user.password == form.password.data:
                    session['logged_in'] = True
                    session['user_id'] = user.id
                    session['username'] = user.username
                    flash(f'Bem vindo, {user.username}', 'success')
                    return redirect(url_for('index_dashboard'))
                else:
                    flash('Senha incorreta', 'danger')
            else:
                flash('Usuario nao encontrado', 'danger')
    return render_template('login/index.html', form=form)


@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in')
    session.pop('user_id')
    session.pop('username')
    return redirect(url_for('login'))