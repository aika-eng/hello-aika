from main import app
from flask import render_template #usado para renderizar as templates de html

@app.route("/") #a barra "/" representa a pasta raiz (home) do site 
def home(): #a função está associada a rota
    return render_template('formulario.html')

@app.route("/contato")
def contato():
    return "Gustavo, telefone 11 99194 6026"