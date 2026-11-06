
# Importando bibliotecas

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


# Criando instâncias das extensões

db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
login_manager: LoginManager = LoginManager()


# Configurações padrão da aplicação

default_page_config: dict[str, str] = {
    "title": "Docly",
    "description": "Gestão documental simples, organizada e segura.",
}


# Carregando o usuário autenticado

@login_manager.user_loader
def load_user(user_uuid: str):

    from app.models.users import User

    return db.session.execute(
        db.select(User).filter_by(uuid=user_uuid)
    ).scalar_one_or_none()
