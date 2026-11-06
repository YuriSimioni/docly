
# Importando bibliotecas

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

auth_bp = Blueprint('auth', __name__)


# Definindo a rota de login

@auth_bp.route('/', methods=['GET', 'POST'])
def login():

    # Verificando se o usuário já está autenticado
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))

    if request.method == 'POST':

        login = request.form.get('login', '').strip()
        password = request.form.get('password', '')

        user = UserService.authenticate_user(login, password)

        if user:

            # Iniciando a sessão do usuário
            login_user(user)

            flash("Login realizado com sucesso.", "success")

            # Verificando redirecionamento solicitado
            next_page = request.args.get('next')

            if next_page:
                parsed_url = urlparse(next_page)

                if parsed_url.netloc or parsed_url.scheme:
                    next_page = None

            return redirect(
                next_page or url_for('auth.dashboard')
            )

        # Autenticação falhou
        flash("Login ou senha inválidos.", "error")

        return render_template(
            'auth/login.html',
            base_page=extensions.default_page_config,
            page_title="Login",
            message="Login ou senha inválidos."
        )

    return render_template(
        'auth/login.html',
        base_page=extensions.default_page_config,
        page_title="Login"
    )


# Definindo a rota do dashboard

@auth_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():

    return render_template(
        'dashboard.html',
        base_page=extensions.default_page_config,
        page_title="Dashboard",
        sidebar_selected="dashboard"
    )


# Definindo a rota de logout

@auth_bp.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():

    logout_user()

    flash("Você saiu da sua conta.", "success")

    return redirect(url_for('auth.login'))
