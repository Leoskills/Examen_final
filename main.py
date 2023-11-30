from flask import Flask, render_template, request

app = Flask(__name__)

usuarios = {
    "juan": "admin",
    "pepe": "user"
}


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def calculoCompras():
    if request.method == 'POST':
        nombre = request.form['nombre']
        años = int(request.form['años'])
        cantidad = int(request.form['cantidad'])
        cost_per_tar = 9000
        total_sin_descuento = cost_per_tar * cantidad

        descuento = 0
        if 18 <= años <= 30:
            descuento = 0.15
        elif años > 30:
            descuento = 0.25

        total = total_sin_descuento - (total_sin_descuento * descuento)

        return render_template('ejercicio1.html', total_sin_descuento=total_sin_descuento, total=total, nombre=nombre, años=años, cantidad=cantidad, descuento=descuento)
    return render_template('ejercicio1.html')


@app.route('/Ejercicio3', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        if usuario in usuarios and usuarios[usuario] == contraseña:
            return render_template('Ejercicio3.html', nombre=usuario, rol='administrador' if usuario == 'juan' else 'usuario')
        else:
            error = 'Usuario o contraseña incorrecta'

    return render_template('Ejercicio3.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)