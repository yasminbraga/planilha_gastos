from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import fields, validators



class LoginForm(FlaskForm):
    username = fields.StringField('Username', validators=[validators.DataRequired()])
    password = fields.PasswordField('Senha', validators=[validators.DataRequired()])
