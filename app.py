"""
Simple flask app
"""
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    """ root endpoint """
    # return '<h1>Index page</h1>'
    return render_template('index.html')

@app.route("/hola/")
@app.route("/hola/<nombre>")
def hola(nombre='Anonimo'):
    """ hola """
    return render_template('hola.html', nombre = nombre)

@app.route("/hola-formulario")
def hola_formulario():
    """ hola formulario """
    return render_template('hola-formulario.html')

@app.route("/hola-action", methods=['POST'])
def hola_action():
    """ hola action """
    nombre = request.form['nombre']
    return render_template('hola-action.html', nombre=nombre)

@app.route("/api/hola-action", methods=['POST'])
def api_hola_action():
    nombre = request.json['nombre'].upper()
    return jsonify({'nombre': nombre})
