from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='views')


def init_app(app):

    listaFilmes = [{'nome': 'Pobres Criaturas', 'diretor': 'Yorgos Lanthimos', 'dataLan': '25/01/2024', 'sinopse' : ''}, 
                   {'nome' : 'Saneamento Básico, O Filme',  'diretor' : 'Jorge Furtado', 'dataLan' : '20/07/2007', 'sinpose' : '' },
                   {'nome' : 'Marty Supreme',  'diretor' : 'Josh Safdie', 'dataLan' : '25/12/2025', 'sinpose' : '' },
                   {'nome' : 'Look Back',  'diretor' : 'Kiyotaka Oshiyama', 'dataLan' : '28/06/2024', 'sinpose' : '' },
                   ]
    listaSerie = [{'nome': 'Dark', 'diretor': 'Baran bo Odar', 'dataLan': '1/12/2017', 'sinopse' : ''}, 
                   {'nome' : 'Bojack Horseman',  'diretor' : 'Raphael Bob-Waksberg,', 'dataLan' : '22/08/2014', 'sinpose' : '' },
                   {'nome' : 'Breaking Bad',  'diretor' : 'Vince Gilligan', 'dataLan' : '20/08/2008', 'sinpose' : '' },
                   {'nome' : 'Your Lie in April',  'diretor' : 'Kyohei Ishiguro', 'dataLan' : '9/10/2014', 'sinpose' : '' },
                   ]
    
    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    @app.route('/formFilmes', methods=['GET', 'POST'])
    def formFilmes():
        if request.method == 'POST':
            listaFilmes.append({'nome': request.form.get('nome'), 'diretor': request.form.get(
                'diretor'), 'dataLan': request.form.get('dataLan'), 'sinopse': request.form.get('sinopse')})
            return redirect(url_for('list'))
        return render_template('formularioFilme.html', listaFilmes = listaFilmes)
    
    
    @app.route('/formSeries', methods=['GET', 'POST'])
    def formSeries():
        if request.method == 'POST':
            listaSerie.append({'nome': request.form.get('nome'), 'diretor': request.form.get(
                'diretor'), 'dataLan': request.form.get('dataLan'), 'sinopse': request.form.get('sinopse')})
            return redirect(url_for('list'))
        return render_template('formularioSerie.html', listaSerie = listaSerie)

    @app.route('/list', methods=['GET', 'POST'])
    def list():
        return render_template('lista.html', listaFilmes = listaFilmes, listaSerie = listaSerie)
