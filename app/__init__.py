
# Importando as bibliotecas necessárias

from flask import Flask

from app.core.config import Config
from app.core.extensions import db, migrate, login_manager

# Função para criar a aplicação Flask

def create_app() -> Flask:

    # Criando a instância da aplicação
    app: Flask = Flask(__name__)

    # Configurando a aplicação
    app.config.from_object(Config)

    # Inicializando as extensões
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Configurações Flask-Login
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Faça login para acessar esta página.'
    login_manager.login_message_category = 'warning'

    # Importando os modelos para registrar no SQLAlchemy
    from app.models.users import User

    # Registrando os blueprints
    from app.routes.auth import auth_bp
    from app.routes.admin import admin_bp
    from app.routes.documents import document_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(document_bp)

    return app
