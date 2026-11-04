# Importando as bibliotecas necessárias
from flask import Flask
from app.auth.security import hash_password
from app.core.config import Config
from app.core.extensions import db, migrate

# Função para criar a aplicação Flask
def create_app() -> Flask:

    # Criando a instância da aplicação Flask
    app: Flask = Flask(__name__)
    app.secret_key = Config.SECRET_KEY

    # Configurando a aplicação Flask com as variáveis de ambiente
    app.config.from_object(Config)

    # Iniciando as extensões do Flask
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Importando os modelos do banco de dados
    from app.models.users import User
    
    # Inicializando o banco de dados
    with app.app_context():
        db.create_all()


    # Registrando os blueprints das rotas
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    # Retornando a aplicação
    return app