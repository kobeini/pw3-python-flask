# Importando o Flask para a aplicação
from flask import Flask, render_template
from controllers import routes
# Carregando o Flask na variável "app"

app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente 
# __name__ representa o nome da aplicação

#Enviar variável APP para rotas
routes.init_app(app)

# Rota Principal do Site
# @ serve para ligar a rota a função que vem abaixo dela
# Servidor python sempre abre na porta 5000
if __name__ == '__main__':
    # Verificando se o arquivo __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# Método .run() inicia o servidor
