from flask import Flask, render_template, request
from calculadora import calcular

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.method == 'POST': 
        return calcular()
    return render_template('calculadora.html', etapas = '', resultados = '')


@app.route('/calculadoracientifica', methods = ['GET', 'POST'])
def calculadoracientifica():
    if request.method == 'POST': 
        return calcular()
    return render_template('calculadoracientifica.html', etapas = '', resultados = '')

if __name__ == '__main__':
    app.run(debug=True)