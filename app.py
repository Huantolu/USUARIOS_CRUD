from flask import Flask, request, url_for, redirect, render_template
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "ABCDEFGHIJKMNOPQRSTUVWXYZ"

#Definir la primera ruta
@app.route('/')
def from inicio():
    usuarios = Usuario.get_all()
    return render_template("index.html", usuarios=usuarios)

