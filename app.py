from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Portal de Tecnologia e Computação")



if __name__ == '__main__':
    app.run(debug=True)
