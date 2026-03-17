
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='views')


def init_app(app):

    listaConsoles = ['Playstation 5', 'Xbox One',
            'Super Nintendo', 'Atari 2600', 'Nintendo 3DS']


    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        # Criar informação para a rota de games
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        jogadores = ['Marcos', 'Richard', "Miguel", 'Renato', 'Pedro']
        return render_template('games.html', titulo=titulo, ano=ano, categoria=categoria, jogadores=jogadores)

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # criando um objeto
        console = {"Nome:": "Playstation 2 ",
                   "Fabricante: ": "Sony", "Ano: ": 2000}
        #Recebendo o valor do formulário
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
        
        return render_template('consoles.html', console=console, listaConsoles=listaConsoles)
