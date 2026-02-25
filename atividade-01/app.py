from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='views')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('formulario.html')

@app.route('/list')
def list():
    return render_template('lista.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)