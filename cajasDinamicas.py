from flask import Flask, render_template
from flask import request


app=Flask(__name__)


@app.route("/")
def formulario():
    return render_template("indexCajas.html")

@app.route("/cajasForm", methods=['POST'])
def cajas():
    num = request.form.get('numeroCajas')
    return render_template("cajasForm.html", cajas=int(num))

@app.route("/resultado", methods=['POST'])
def resultado():
    numerosProcesados = []
    numeros = request.form
    print(len(numeros))
    i = 1
    while i <= len(numeros):
        numerosProcesados.append(numeros.get('txtCaja'+str(i)))
        i += 1
    print(numerosProcesados)

    #sacar el numero menor y mayor de la lista numeros procesados
    mayor = 0
    menor = int(numerosProcesados[0])
    suma = 0
    for i in numerosProcesados:
        suma += int(i)
        if int(i) > mayor:
            mayor = int(i)
        if int(i) < menor:
            menor = int(i)

    print(mayor)
    print(menor)
    promedio = suma / len(numerosProcesados)
    print(promedio)

    #saber si un numero se repite mas de 1 vez
    repetidos = []
    for i in numerosProcesados:
        if numerosProcesados.count(i) > 1:
            texto = "El numero " + i + " se repite " + str(numerosProcesados.count(i)) + " veces"
            if texto not in repetidos:
                repetidos.append(texto)
    print(repetidos)

    return render_template("resultado.html",suma=suma, mayor=mayor, menor=menor, promedio=promedio, repetidos=repetidos,numerosIngresados=len(numerosProcesados))




if __name__=="__main__":
    app.run(debug=True)