# Importando as bibliotecas necessárias
from flask import Flask
from app.core.config import Config
from app.core.extensions import db, migrate

# Função para criar a aplicação Flask
def create_app() -> Flask:

    # Criando a instância da aplicação Flask
    app: Flask = Flask(__name__)

    # Configurando a aplicação Flask com as variáveis de ambiente
    app.config.from_object(Config)

    # Iniciando as extensões do Flask
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Inicializando o banco de dados
    with app.app_context():
        db.create_all()

    # Definindo uma rota de teste para verificar se a aplicação está funcionando
    @app.route("/")
    def index():
        return "Hello, World!"

    # Retornando a aplicação
    return app