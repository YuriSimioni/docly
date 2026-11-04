# Importando bibliotecas
from flask import Blueprint, render_template

from app.core import extensions

# Criando o blueprint para a rota de autenticação
auth_bp = Blueprint('auth', __name__)

# Definindo a rota de login
@auth_bp.route('/')
def login():
    return render_template('auth/login.html',
                           base_page=extensions.default_page_config,
                           page_title="Login"
                           )