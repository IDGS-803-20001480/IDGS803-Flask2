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
    numeros = request.form
    print(numeros)
    return render_template("resultado.html", numeros=int(numeros))




if __name__=="__main__":
    app.run(debug=True)