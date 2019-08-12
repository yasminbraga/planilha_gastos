from flask import render_template, request, url_for, redirect
from app import app, db
from app.models.models import User

@app.route('/users')
def index_users():
    users = User.query.all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def new_users():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(name=name, email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index_users'))
    return render_template('users/new.html')


@app.route('/users/edit/<int:id>', methods=['GET', 'POST'])
def edit_users(id):
    user = User.query.get(id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        user.name = name
        user.email = email
        user.username = username
        user.password = password

        db.session.commit()
        return redirect(url_for('index_users'))
    return render_template('users/edit.html', user=user)


@app.route('/users/delete/<int:id>')
def delete_users(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index_users'))

