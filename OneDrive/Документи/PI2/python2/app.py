from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html')  # Adicione a página 'projeto.html' correspondente

@app.route('/documentacao')
def documentacao():
    return render_template('documentacao.html')  # Adicione a página 'documentacao.html' correspondente

@app.route('/modulos')
def modulos():
    return render_template('modulos.html')

@app.route('/processamento')
def processamento():
    return render_template('processamento.html')


@app.route('/explo')
def explo():
    return render_template('explo.html')

if __name__ == '__main__':
    app.run(debug=True)
