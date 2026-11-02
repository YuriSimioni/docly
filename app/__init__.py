# Importando bibliotecas
from flask import Flask

# Função para criar a aplicação Flask
def create_app():
    
    # Criando a instância da aplicação Flask
    app: Flask = Flask(__name__)
    
    # Definindo uma rota de teste para verificar se a aplicação está funcionando
    @app.route("/")
    def index():
        return "Hello, World!"
    
    # Retornando a instância da aplicação Flask
    return app