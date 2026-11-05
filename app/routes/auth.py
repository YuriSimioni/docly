# Importando bibliotecas


from flask import Blueprint, render_template, request, flash

from app.core import extensions
from app.services.users import UserService

# Criando o blueprint para a rota de autenticação
auth_bp = Blueprint('auth', __name__)

# Definindo a rota de login
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login') or ''
        password = request.form.get('password') or ''
        
        user = UserService.authenticate_user(login, password)
        
        if user:
            # Autenticação bem-sucedida
            flash("Login realizado com sucesso.", "success")
            return render_template('dashboard.html',
                                   base_page=extensions.default_page_config,
                                      page_title="Login",
                                      message="Login realizado com sucesso."
                                      )
        else:
            flash("Login ou senha inválidos.", "error")
            # Autenticação falhou
            return render_template('auth/login.html',
                                   base_page=extensions.default_page_config,
                                   page_title="Login",
                                   message="Login ou senha inválidos."
                                   )
        
    return render_template('auth/login.html',
                           base_page=extensions.default_page_config,
                           page_title="Login"
                           )
    
@auth_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html',
                           base_page=extensions.default_page_config,
                           page_title="Dashboard",
                           sidebar_selected="dashboard"
                           )