from flask import Flask
from rotas import rotas  # Importa o blueprint de rotas

app = Flask(__name__)

# Registra o blueprint de rotas
app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True)
