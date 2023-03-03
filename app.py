from flask import Flask, render_template
from flask import request
import forms
from flask_wtf import CSRFProtect #importamos la libreria para proteger el formulario
from flask import make_response #importamos la libreria para crear cookies
from flask import flash #importamos la libreria para mostrar mensajes

app=Flask(__name__)
app.config['SECRET_KEY']= "Esta es la clave encriptadora"
csrf = CSRFProtect()

#-----------------------Cokiees--------------------------------
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



#-----------------------Traductor archivo de texto--------------------------------


@app.route("/traductor", methods=['GET', 'POST'])
def traductor():
    respuesta=""
    trad_form = forms.TraductorForm(request.form)
    trad_form_response = forms.TraductorFormRespose(request.form)
    if request.method == 'POST' and trad_form.validate():
        f=open("Traductor.txt", "a")
        f.write("\n"+ ""+trad_form.palabra.data+"="+trad_form.traduccion.data+"")
        f.close()
        respuesta = trad_form.palabra.data
        print(trad_form.palabra.data)
        print(trad_form.traduccion.data)
    return render_template("traductor.html",respAdd=respuesta,form=trad_form,form2=trad_form_response)

@app.route("/traductor_response", methods=['GET', 'POST'])
def traductor_response():
    respuesta=""
    trad_form = forms.TraductorForm(request.form)
    trad_form_response = forms.TraductorFormRespose(request.form)
    if request.method == 'POST' and trad_form_response.validate():
        palabra = trad_form_response.palabra_Traducir.data
        opc = trad_form_response.radioIdiomaTraducir.data
        print(palabra+" idioma:"+opc)
        if opc=="es":
            f=open("Traductor.txt", "r")
            listaTraductor = f.readlines()
            for linea in listaTraductor:
              palabraIndicador=str(linea.split("=")[0])
              if palabraIndicador == palabra:
                  print(linea)
                  print(linea.split("=")[1])
                  respuesta=linea.split("=")[1]
            f.close()
            if respuesta == "":
                respuesta = "No se encontro la palabra"
            print(respuesta)
            
        elif opc=="en":
            print("Ingles")
            f=open("Traductor.txt", "r")
            listaTraductor = f.readlines()
            for linea in listaTraductor:
                palabraIndicador=str(linea.split("=")[1])
                palabraIndicador= palabraIndicador.strip()
                print(palabraIndicador+"n")
                if palabraIndicador == palabra:
                    print(linea)
                    print(linea.split("=")[0])
                    respuesta=linea.split("=")[0]
            f.close()
            if respuesta == "":
                respuesta = "No se encontro la palabra"
            print(respuesta)
    return render_template("traductor.html",resp=respuesta,entrada = palabra,form2=trad_form_response,form=trad_form)

#-----------------------Calculadora de resistencias--------------------------------
@app.route("/resistencias", methods=['GET', 'POST'])
def resistencias():
    colores = [("0","black"),("1","brown"),("2","red"),("3","orange"),("4","yellow"),("5","green"),("6","blue"),("7","violet"),("8","grey"),("9","white")]
    coloresMultiplicador = [("1","black"),("10","brown"),("100","red"),("1000","orange"),("10000","yellow"),("100000","green"),("1000000","blue"),("10000000","violet"),("100000000","grey"),("1000000000","white"),("0.1","gold"),("0.01","silver")]
    coloresTolerancia = [("1","brown"),("2","red"),("0.5","green"),("0.25","blue"),("0.1","violet"),("0.05","grey"),("5","gold"),("10","silver")]
    color1 = ""
    color2 = ""
    colorMulti = ""
    colorTol = ""
    max = 0
    min = 0
    result = 0
    resistencia_form = forms.ResistenciaForm(request.form)
    if request.method == 'POST' and resistencia_form.validate():
        
        for color in colores:
            if color[0] == resistencia_form.linea1.data:
                color1 =  color[1]
            if color[0] == resistencia_form.linea2.data:
                color2 = color[1]
        for color in coloresMultiplicador:
            if color[0] == resistencia_form.lineaMultiplicador.data:
                colorMulti = color[1]
        for color in coloresTolerancia:
            if color[0] == resistencia_form.lineaTolerancia.data:
                colorTol = color[1]

        
        result = ((int(resistencia_form.linea1.data)*10) + int(resistencia_form.linea2.data))*float(resistencia_form.lineaMultiplicador.data)
        min = result * (1-(float(resistencia_form.lineaTolerancia.data)/100))
        max = result * (1+(float(resistencia_form.lineaTolerancia.data)/100))
        print("Resultado: "+str(result))
        print("Minimo: "+str(min))
        print("Maximo: "+str(max))
        print("Color 1: "+color1)
        print("Color 2: "+color2)
        print("Color Multiplicador: "+colorMulti)
        print("Color Tolerancia: "+colorTol)
    return render_template("calculadoraResistencias.html",form=resistencia_form,banda1=color1,banda2=color2,bandaMulti=colorMulti,bandaTol=colorTol,resultado=result,minimo=min,maximo=max)


if __name__=="__main__":
    csrf.init_app(app)
    app.run(debug=True)