from flask import Flask, render_template,request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/notas", methods= ["GET","POST"])
def nota():
    promedio = 0
    asistencia = None
    if request.method == "POST":
        nota1 = int(request.form["nota1"])
        nota2 = int(request.form["nota2"])
        nota3 = int(request.form["nota3"])
        asistencia = int(request.form["asistencia"])

        promedio= (nota1+nota2+nota3)/3


    return render_template("notas.html", promedio=promedio, asistencia=asistencia)



@app.route("/nombres", methods= ["GET","POST"])
def nombre():
    mas_len = None
    count = None
    if request.method == "POST":
        nombre1 = str(request.form["nombre1"])
        nombre2 = str(request.form["nombre2"])
        nombre3 = str(request.form["nombre3"])
        
        if len(nombre1)> len(nombre2) and len(nombre1)> len(nombre3):
            mas_len=nombre1
            count = len(nombre1)
            #return render_template("notas.html", mas_len=mas_len, count = count)
        elif len(nombre2)> len(nombre1) and len(nombre2)> len(nombre3):
            mas_len=nombre2
            count = len(nombre2)
            #return render_template("notas.html", mas_len = mas_len,count = count)
        else:
            mas_len=nombre3
            count = len(nombre3)
           #return render_template("notas.html", mas_len=mas_len, count = count)
    return render_template("nombres.html", mas_len=mas_len, count = count)
        


if __name__ == '__main__':
    app.run(debug=True)