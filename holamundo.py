from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('home.html', title='Página de Inicio')

@app.route('/apruebo')
def apruebo():
    return render_template('apruebo.html', title='Acción Aprobada')

@app.route('/comprobado')
def comprobado():
    return render_template('comprobado.html', title='Acción Comprobada')

if __name__ == '__main__':
    app.run(debug=True, port=5600)
