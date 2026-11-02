# Importando a função create_app do módulo app
from app import create_app

# Criando a instância da aplicação Flask
if __name__ == "__main__":
    
    # Chamando a função create_app para criar a aplicação Flask
    app = create_app()
    
    # Iniciando o servidor da aplicação Flask
    app.run(host='0.0.0.0', port=5000, debug=True)
    