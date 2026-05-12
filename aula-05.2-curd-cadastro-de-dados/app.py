# Importando o Flask para a aplicação
from flask import Flask, render_template
from controllers import routes
from models.database import db
import pymysql
# Carregando o Flask na variável "app"


app = Flask(__name__, template_folder='views')
# Variáveis com __ são variáveis de ambiente 
# __name__ representa o nome da aplicação

DB_NOME = 'thegames'

app.config['DATABASE_NAME'] = DB_NOME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NOME}'



#Enviar variável APP para rotas
routes.init_app(app)

# Rota Principal do Site
# @ serve para ligar a rota a função que vem abaixo dela
# Servidor python sempre abre na porta 5000
if __name__ == '__main__':
    # Conectando-se ao MYSQL para criar o banco de dados 
    connection = pymysql.connect(host='localhost', user='root',password='', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute (f'CREATE DATABASE IF NOT EXISTS {DB_NOME}')
            print("O banco de dados está criado!")
    except Exception as error:
        print(f"Ocorreu um erro ao criar o banco de daods! {error}")
    finally:
        connection.close()
        
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    # Verificando se o arquivo __name__ é o arquivo principal
    app.run(port=5000, debug=True)
# Método .run() inicia o servidor
