from flask import Flask, request, url_for, redirect, render_template
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "ABCDEFGHIJKMNOPQRSTUVWXYZ"

#Definir la primera ruta
@app.route('/')
def inicio():
    usuarios = Usuario.get_all()
    return render_template("index.html", usuarios = usuarios)

#Definir la ruta para crear un nuevo usuario
@app.route("/nuevo_usuario")
def form_usuario():
    return render_template("registro.html")

#Donde se ingresan los datos del nuevo usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    email = request.form["email"]

@app.route("/editar/<int:id>")
def editar_usuario(user_id):
    datos = {"id": user_id}
    usuario = Usuario.get_by_id(datos)
    return render_template("configuracion.html", usuario = usuario)

@app.route("/editar_usuario", methods=["POST"])
def editar_usuario(user_id):
    datos = {
        "id": user_id,
        "nombre": request.form["nombre"],
        "apellido": request.form["apellido"],
        "email": request.form["email"]
    }
    Usuario.update(datos)
    return redirect(f"/usuario/{user_id}")

@app.route("/usuario")
def usuario():
    render_template("usuario.html")

@app.route("/usuario/<int:id>")
def usuario(user_id):
    datos = {"id": user_id}
    usuario = Usuario.get_by_id(datos)
    return render_template("usuario.html", usuario = usuario)

@app.route("/eliminar/<int:id>")
def eliminar_usuario(user_id):
    datos = {"id": user_id}
    Usuario.delete(datos)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)