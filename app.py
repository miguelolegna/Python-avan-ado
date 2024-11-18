import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask import Flask, render_template
from rotas import rotas  # Importa o blueprint de rotas

app = Flask(__name__)

# Configuração do Cloudinary
cloudinary.config(
    cloud_name="dsffb07j5",
    api_key="879557861268383",
    api_secret="t7DxBBfnn9pu7XQBjuAMbzNQm68"
)

# Rotas principais
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/processamento')
def processamento():
    return render_template('processamento.html')

@app.route('/explo')
def explo():
    return render_template('explo.html')

# Registra o blueprint de rotas
app.register_blueprint(rotas)

if __name__ == '__main__':
    app.run(debug=True)
