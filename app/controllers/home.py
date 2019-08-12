from app import app
from flask import render_template, url_for


@app.route('/home')
def index_home():
    return render_template('home/index.html')