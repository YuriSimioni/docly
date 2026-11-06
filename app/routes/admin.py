
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

admin_bp = Blueprint('admin', __name__, url_prefix="/admin")


# Definindo a rota do dashboard

@admin_bp.route('/', methods=['GET'])
@login_required
def dashboard():

    return render_template(
        'admin/dashboard.html',
        base_page=extensions.default_page_config,
        page_title="Painel Administrativo",
        sidebar_selected="admin_panel",
        users_list=UserService.list_all_users()
    )
    
    


@admin_bp.route('/users/register', methods=['POST'])
@login_required
def register_user():

    # Capturando os dados do formulário
    name = request.form.get('name')
    surname = request.form.get('surname')
    login = request.form.get('login')
    password = request.form.get('password')
    email = request.form.get('email')

    try:
        UserService.register_user(
            name,
            surname,
            login,
            password,
            email
        )

        flash("Usuário cadastrado com sucesso!", "success")

    except UserAlreadyExistsError as error:
        flash(str(error), "warning")

    except Exception:
        current_app.logger.exception(
            "Erro inesperado ao cadastrar usuário."
        )
        flash("Ocorreu um erro ao cadastrar o usuário.", "error")

    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/users/delete/<uuid>', methods=['POST', 'GET'])
@login_required
def delete_user(uuid):

    try:
        UserService.delete_user(uuid)

        flash("Usuário deletado com sucesso!", "success")

    except Exception:
        current_app.logger.exception(
            "Erro inesperado ao deletar usuário."
        )
        flash("Ocorreu um erro ao deletar o usuário.", "error")

    return redirect(url_for('admin.dashboard'))