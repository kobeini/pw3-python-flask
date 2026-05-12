#Importando o flask para a aplicação
from flask import  render_template, request, redirect, url_for
from models.database import Game, db, Console


def init_app(app):
    listaConsoles = ['Playstation 5', 'xbox One', 'Super Nintendo', 'Atari', '3DS',]
    listaGames = [{'titulo' : 'CS-GO', 'ano': 2012, 'categoria': 'FPS online', 'plataforma': 'PC (Windows)'}]
    @app.route('/')
    def home():
        return render_template('index.html')
    @app.route('/games')
    def games():
        titulo = "Portal 2"
        ano = 2011
        categoria = "Puzzle"
        jogadores = ['Marcos', 'Richard', 'Miguel', 'Renato', 'Pedro']
        
        return render_template('games.html',
                            titulo = titulo,
                            ano = ano,
                            categoria = categoria,
                            jogadores=jogadores )

    @app.route('/consoles', methods=['GET', 'POST'])
    def consoles():
        # Criando um objeto
        console = {"Nome" : "Playstation 2",
                "Fabricante" : "Sony",
                "Ano" : 2000}
        if request.method == 'POST':
            if request.form.get('novoConsole'):
                listaConsoles.append(request.form.get('novoConsole'))
                

        return render_template('consoles.html',
                            console = console,
                            listaConsoles = listaConsoles)
        
    @app.route("/cadgames", methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST':
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria'), 'plataforma': request.form.get('plataforma')})
            return redirect(url_for('cadgames'))
            
        return render_template('cadastrar.html',
                                listaGames = listaGames)
        
    @app.route('/estoque', methods=['GET', 'POST'])
    def estoque():
        if request.method == 'POST':
            dados = request.form.to_dict()
            newgame = Game(
                dados['titulo'],
                dados['ano'],
                dados['categoria'],
                dados['plataforma'],
                dados['preco'],
                dados['quantidade']
            )
            db.session.add(newgame)
            db.session.commit()
            return redirect(url_for('estoque'))
        games = Game.query.all()
        return render_template('estoque.html', games=games)
    
    @app.route('/estoque_console', methods=['GET', 'POST'])
    def estoque_console():
        if request.method == 'POST':
            dados = request.form.to_dict()
            newconsole = Console(
                dados['nome'],
                dados['fabricante'],
                dados['ano'],
                dados['preco'],
             
            )
            db.session.add(newconsole)

            db.session.commit()
            return redirect(url_for('estoque_console'))
        consoles = Console.query.all()
        return render_template('estoque_console.html', consoles=consoles)