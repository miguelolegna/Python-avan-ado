from flask import Flask, render_template
from flask_assets import Environment, Bundle

app = Flask(__name__)

# Configurar Flask-Assets
assets = Environment(app)

# Definir um bundle para o SCSS
scss = Bundle('scss/styles.scss', filters='libsass', output='scss/styles.css')
assets.register('scss_all', scss)

# Rotas
@app.route('/') 
def index():
    return render_template('index.html')


@app.route('/Documentação')  
def Documentação():
    return render_template('/Documentação.html')

@app.route('/API')  
def API():
    return render_template('API.html')

@app.route('/AI')  
def AI():
    return render_template('AI.html')

@app.route('/tecnologia')  
def tecnologia():
    return render_template('tecnologia.html')


@app.route('/detalhes')  
def detalhes():
    return render_template('detalhes.html')
    

@app.route('/java')  
def java():
    return render_template('java.html')

@app.route('/python') 
def python():
    return render_template('python.html')

@app.route('/cpp')    
def cpp():
    return render_template('cpp.html')

@app.route('/db')    
def database():
    return render_template('db.html')

@app.route('/reds')  
def networks():
    return render_template('reds.html')

@app.route('/pross-comp')  
def computing():
    return render_template('pross-comp.html')

# Iniciar o app
if __name__ == '__main__':
    app.run(debug=True)
