
# Importando bibliotecas
from app.exceptions.users import UserAlreadyExistsError
from flask import Response, current_app
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for
)

from flask_login import (
    login_user,
    logout_user,
    login_required,
    current_user
)

from urllib.parse import urlparse

from app.core import extensions
from app.services.users import UserService


# Criando o blueprint para a rota de autenticação

document_bp = Blueprint('docs', __name__, url_prefix="/my-docs")


# Definindo a rota do dashboard

@document_bp.route('/', methods=['GET'])
@login_required
def dashboard():

    return render_template(
        'docs/dashboard.html',
        base_page=extensions.default_page_config,
        page_title="Meus Documentos",
        sidebar_selected="documents",
        
    )