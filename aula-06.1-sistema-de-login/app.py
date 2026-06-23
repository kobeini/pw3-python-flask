from flask import Flask, render_template
import pymysql
from models.database import db, Game
from controllers import routes

DB_NAME = 'thegames'
 
app = Flask(__name__, template_folder='views')
app.config['DATABASE_NAME'] = DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root@localhost/{DB_NAME}'
routes.init_app(app)

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            cursor.execute(f'CREATE DATABASE IF NOT EXISTS {DB_NAME}')
            print("o banco de dados está criado!")
    except Exception as error:
        print(f"Ocorreu um erro ao criar o banco de dados!' {error}")

    finally:
        connection.close()
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(port=5000, debug=True)