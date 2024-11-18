from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quienes-somos")
def quienes_somos():
    return render_template("quienes-somos.html")

@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():
    resultado = None
    if request.method == "POST":
        try:
            # obtenemos los datos del formulario por el metodo post
            nota1 = float(request.form["nota1"])
            nota2 = float(request.form["nota2"])
            nota3 = float(request.form["nota3"])
            asistencia = float(request.form["asistencia"])

            # se calcula el promedio
            promedio = (nota1 + nota2 + nota3) / 3

            # se utiliza la condicional if para ver si esta Aprobado o Reprobado
            if promedio >= 40 and asistencia >= 75:
                estado = "Aprobado"
            else:
                estado = "Reprobado"

            resultado = {"promedio": promedio, "estado": estado}
        except ValueError:
            resultado = {"error": "Por favor, ingresa valores numéricos válidos."}

    return render_template("ejercicio1.html", resultado=resultado)

@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():
    resultado = None
    if request.method == "POST":
        # se obtienen los nombres mediante el metodo post
        nombre1 = request.form["nombre1"]
        nombre2 = request.form["nombre2"]
        nombre3 = request.form["nombre3"]

        # utilizo la funcion len para obetener el largo de los nombres
        nombres = [(nombre1, len(nombre1)), (nombre2, len(nombre2)), (nombre3, len(nombre3))]
        # y la funcion max para obtener el nombre con mayor longitud
        nombre_mas_largo = max(nombres, key=lambda x: x[1])

        resultado = {"nombre": nombre_mas_largo[0], "longitud": nombre_mas_largo[1]}

    return render_template("ejercicio2.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
