# Importando bibliotecas
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Criando instâncias do SQLAlchemy e do Migrate
db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()
default_page_config: dict[str, str] = {
    "title": "Docly",
    "description": "Gestão documental simples, organizada e segura.",
}