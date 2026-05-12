from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# CRIAR CLASSE PARA REPRESENTAR UMA ENTIDADE EM UM BANCO


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255))
    ano = db.Column(db.Integer)
    categoria = db.Column(db.String(255))
    plataforma = db.Column(db.String(255))
    preco = db.Column(db.Float)
    quantidade = db.Column(db.Integer)

    # iniciar as variáveis em um metodo construtor


    def __init__(self, titulo, ano, categoria, plataforma, preco, quantidade):
        self.titulo = titulo
        self.ano = ano
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade

class Console(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    fabricante = db.Column(db.String(150))
    ano = db.Column(db.Integer)
    preco = db.Column(db.Float)
    
    def __init__(self, nome, fabricante, ano, preco):
        self.nome = nome
        self.fabricante = fabricante
        self.ano = ano
        self.preco = preco
