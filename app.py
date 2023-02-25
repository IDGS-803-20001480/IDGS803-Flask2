from flask import Flask, render_template
from flask import request
import forms
from flask_wtf import CSRFProtect #importamos la libreria para proteger el formulario
from flask import make_response #importamos la libreria para crear cookies
from flask import flash #importamos la libreria para mostrar mensajes

app=Flask(__name__)
app.config['SECRET_KEY']= "Esta es la clave encriptadora"
csrf = CSRFProtect()

@app.route("/cookies",methods=['GET', 'POST'])
def cookies():
    reg_user=forms.LoginForm(request.form)
    datos = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.username.data
        passw = reg_user.password.data
        datos = user + '@' + passw
        success_mensaje = "Bienvenido {}".format(user)
        flash(success_mensaje)
        print(datos)
    response = make_response(render_template("cookies.html", form=reg_user))
    if len(datos)>0:
        response.set_cookie('datos_user', datos)

    return response

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('datos_user')
    nombres=valor_cookie.split('@')
    return render_template("saludo.html", nom=nombres[0])


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(alum_form.matricula.data)
        print(alum_form.nombre.data)
    return render_template("Alumnos.html",form=alum_form)

if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True)