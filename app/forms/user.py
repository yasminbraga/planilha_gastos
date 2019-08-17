from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import fields, validators


class UserForm(FlaskForm):
    name = fields.StringField('Nome', validators=[validators.DataRequired()])
    username = fields.StringField('Username', validators=[validators.DataRequired()])
    email = EmailField('Email', validators=[validators.DataRequired()])
    password = fields.PasswordField('Senha', validators=[validators.DataRequired()])


class EditUserForm(FlaskForm):
    name = fields.StringField('Nome', validators=[validators.DataRequired()])
    username = fields.StringField('Username', validators=[validators.DataRequired()])
    email = EmailField('Email', validators=[validators.DataRequired()])
    
