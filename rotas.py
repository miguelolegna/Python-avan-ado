from flask import Blueprint, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

rotas = Blueprint('rotas', __name__)

# Lista para armazenar páginas
pages = []

# Rota para listar as páginas
@rotas.route('/')
def index():
    return render_template('index.html', pages=pages)

# Rota para criar uma nova página
@rotas.route('/create_page', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        page_name = request.form['page_name']
        image_file = request.files['image']
        
        if image_file:
            # Salvar imagem
            filename = secure_filename(image_file.filename)
            image_path = os.path.join('static/uploads', filename)
            image_file.save(image_path)
            
            # Adicionar página à lista
            pages.append({'page_name': page_name, 'image_filename': filename, 'image_path': image_path})
        
        return redirect(url_for('rotas.index'))
    
    return render_template('create_page_form.html')

# Rota para visualizar uma página específica
@rotas.route('/<page_name>')
def view_page(page_name):
    page = next((p for p in pages if p['page_name'] == page_name), None)
    
    if page is None:
        return "Página não encontrada", 404
    
    return render_template('new_page.html', page=page)
