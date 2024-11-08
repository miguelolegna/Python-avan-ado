from flask import Flask
from rotas import rotas

app = Flask(__name__)

# Configuração do diretório de upload
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Registrando as rotas
app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True)
