from flask import Blueprint, render_template, request, redirect, url_for
from database import db  # Importa o objeto db de database.py
from datetime import datetime

rotas = Blueprint('rotas', __name__)

# Modelo da tabela de Páginas
class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_name = db.Column(db.String(120), unique=True, nullable=False)
    image_filename = db.Column(db.String(120), nullable=False)
    image_path = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Page {self.page_name}>'

# Função de criação da página
@rotas.route('/create_page', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        page_name = request.form['page_name']
        image_file = request.files['image']
        
        if image_file:
            image_filename = image_file.filename
            image_path = 'static/uploads/' + image_filename
            image_file.save(image_path)

            # Criar uma nova página no banco de dados
            new_page = Page(page_name=page_name, image_filename=image_filename, image_path=image_path)
            db.session.add(new_page)
            db.session.commit()

            return redirect(url_for('rotas.index'))
    return render_template('create_page_form.html')

# Função para a página inicial
@rotas.route('/')
def index():
    pages = Page.query.all()
    return render_template('index.html', pages=pages)

@rotas.route('/page/<int:id>')
def view_page(id):
    page = Page.query.get_or_404(id)
    return render_template('new_page.html', page=page)

