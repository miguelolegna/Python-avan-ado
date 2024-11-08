from flask import Blueprint, render_template, request, redirect, url_for
import os
import json

rotas = Blueprint('rotas', __name__)

# Função para carregar as páginas
def load_pages():
    if os.path.exists('data/pages.json'):
        with open('data/pages.json', 'r') as f:
            return json.load(f)
    return []

# Função para salvar as páginas
def save_pages(pages):
    with open('data/pages.json', 'w') as f:
        json.dump(pages, f)

# Função de criação da página
@rotas.route('/create_page', methods=['GET', 'POST'])
def create_page():
    if request.method == 'POST':
        page_name = request.form['page_name']
        image_file = request.files['image']
        
        if image_file:
            image_filename = image_file.filename
            image_path = os.path.join('static/uploads', image_filename)
            image_file.save(image_path)

            # Adicionar ao JSON
            pages = load_pages()
            new_page = {
                'page_name': page_name,
                'image_filename': image_filename,
                'image_path': image_path
            }
            pages.append(new_page)
            save_pages(pages)

            return redirect(url_for('rotas.index'))  # Redireciona para a página inicial
    return render_template('create_page_form.html')

# Função para visualizar uma página
@rotas.route('/page/<page_name>')
def view_page(page_name):
    pages = load_pages()
    page = next((p for p in pages if p['page_name'] == page_name), None)
    
    if not page:
        return "Página não encontrada", 404

    return render_template('new_page.html', page=page)

# Função para a página inicial
@rotas.route('/')
def index():
    pages = load_pages()
    return render_template('index.html', pages=pages)
