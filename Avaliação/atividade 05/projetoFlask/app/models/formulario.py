from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    senha = PasswordField('senha', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    cnpjcpf = StringField('cpfcnpj', validators=[DataRequired()])


class AttForm(FlaskForm):
    antigo = StringField('email', validators=[DataRequired()])
    novo = PasswordField('senha', validators=[DataRequired()])