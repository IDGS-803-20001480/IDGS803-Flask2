
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, RadioField
from wtforms.fields import EmailField
from wtforms import validators

def mi_validador(form, field):
    if len(field.data)==0:
        raise validators.ValidationError("El campo no tiene datos")

class UserForm(Form):
    matricula= StringField('Matricula', [
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=4, max=15, message='No cumple la longitud para el campo')])
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido')])
    apaterno = StringField('Apaterno',[mi_validador])
    email = EmailField('Correo')


class LoginForm(Form):
    username= StringField('Username', [
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=4, max=15, message='No cumple la longitud para el campo')])
    password = StringField('password',[
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=4, max=15, message='No cumple la longitud para el campo')])
    