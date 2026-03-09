# Importando o Flask para a aplicação
from flask import Flask
from flask import render_template
# Carregando o Flask na variável "app"

app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente 
# __name__ representa o nome da aplicação

# Rota Principal do Site
# @ serve para ligar a rota a função que vem abaixo dela
@app.route('/')
# def cria funções
def home():
    return render_template('index.html')


@app.route('/games')
def games():
    #Criar informação para a rota de games
    titulo = "Portal 2"
    ano = 2011
    categoria = "Puzzle"
    jogadores = ['Marcos', 'Richard', "Miguel", 'Renato', 'Pedro']
    return render_template('games.html', titulo = titulo, ano = ano, categoria = categoria, jogadores = jogadores)


@app.route('/consoles')
def consoles():
    #criando um objeto 
    console = {"Nome:" : "Playstation 2 ", "Fabricante: " : "Sony", "Ano: " : 2000}
    return render_template('consoles.html', console = console)
# Servidor python sempre abre na porta 5000
if __name__ == '__main__':
    # Verificando se o arquivo __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# Método .run() inicia o servidor
