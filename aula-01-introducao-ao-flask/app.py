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
    return render_template('games.html')


@app.route('/consoles')
def consoles():
    return render_template('consoles.html')
# Servidor python sempre abre na porta 5000
if __name__ == '__main__':
    # Verificando se o arquivo __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# Método .run() inicia o servidor
