
from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, RadioField, SelectField
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

class TraductorForm(Form):
    palabra = StringField('Palabra en ingles ', [
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=4, max=15, message='No cumple la longitud para el campo')])
    traduccion = StringField('Traduccion en español',[
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=4, max=15, message='No cumple la longitud para el campo')])

class TraductorFormRespose(Form):
    palabra_Traducir = StringField('Introduce la palabra que quieres traducir', [
        validators.DataRequired(message='El campo es requerido'),validators.Length(min=3, max=15, message='No cumple la longitud para el campo')])
    radioIdiomaTraducir = RadioField('Idioma a traducir',choices=[('es', 'Español'), ('en', 'Ingles')],validators=[validators.DataRequired()],default='es')

class ResistenciaForm(Form):
    #linea 1 de la resistencia de 4 lineas
    colores = [("0","Negro"),("1","Marron"),("2","Rojo"),("3","Naranja"),("4","Amarillo"),("5","Verde"),("6","Azul"),("7","Violeta"),("8","Gris"),("9","Blanco")]
    coloresMultiplicador = [("1","Negro"),("10","Marron"),("100","Rojo"),("1000","Naranja"),("10000","Amarillo"),("100000","Verde"),("1000000","Azul"),("10000000","Violeta"),("0.1","Dorado"),("0.01","Plateado")]
    coloresTolerancia = [("1","Marron"),("2","Rojo"),("0.5","Verde"),("0.25","Azul"),("0.1","Violeta"),("0.05","Gris"),("5","Dorado"),("10","Plateado")]
    linea1 = SelectField("linea 1: ",choices=colores)
    linea2 = SelectField("linea 2: ",choices=colores)
    lineaMultiplicador = SelectField("linea multiplicador: ",choices=coloresMultiplicador)
    lineaTolerancia = SelectField("linea tolerancia: ",choices=coloresTolerancia)