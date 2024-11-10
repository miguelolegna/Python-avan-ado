import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import Flask
from rotas import rotas  # Importa o blueprint de rotas

app = Flask(__name__)

# Configuração do Cloudinary
cloudinary.config(
    cloud_name="dsffb07j5",
    api_key="879557861268383",
    api_secret="t7DxBBfnn9pu7XQBjuAMbzNQm68"
)

# Registra o blueprint de rotas
app.register_blueprint(rotas)

if __name__ == "__main__":
    app.run(debug=True)
