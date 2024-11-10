from flask import Flask
from database import db  # Importa o objeto db do database.py
from rotas import rotas  # Importa o blueprint de rotas

# Cria a instância do aplicativo Flask
app = Flask(__name__)

# Configura o banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa o SQLAlchemy com o aplicativo
db.init_app(app)

# Registra o blueprint de rotas
app.register_blueprint(rotas)

# Cria o banco de dados e as tabelas, se necessário
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
