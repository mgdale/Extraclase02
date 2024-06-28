from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 's3cret.P4ssword1.'  #clave secreta segura

#ruta de la pagina de inicio 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/creaciones')
def creaciones():
    return render_template('creaciones.html')

@app.route('/sobre-mi')
def sobre_mi():
    return render_template('sobre_mi.html')

# ruta de suscripcion
@app.route('/suscribirse')
def suscribirse():
    return render_template('suscribirse.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    name = request.form['name']
    email = request.form['email']
    
    flash('¡Gracias por suscribirte!', 'success')
    
    return f'Gracias por suscribirte, {name}!'

if __name__ == '__main__':
    app.run(debug=True)