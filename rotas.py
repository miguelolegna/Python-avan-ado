from flask import Blueprint, render_template, request, redirect, url_for
import cloudinary.uploader
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
            # Envia a imagem para o Cloudinary
            image = cloudinary.uploader.upload(image_file)
            image_url = image['url']
            image_public_id = image['public_id']
            
            # Adiciona a página à lista
            pages.append({'page_name': page_name, 'image_url': image_url, 'image_public_id': image_public_id})
        
        return redirect(url_for('rotas.index'))
    
    return render_template('create_page_form.html')

# Rota para visualizar uma página específica
@rotas.route('/<page_name>')
def view_page(page_name):
    page = next((p for p in pages if p['page_name'] == page_name), None)
    
    if page is None:
        return "Página não encontrada", 404
    
    return render_template('new_page.html', page=page)

# Rota para excluir uma página
@rotas.route('/delete_page/<page_name>', methods=['POST'])
def delete_page(page_name):
    # Encontrar a página a ser excluída
    page_to_delete = next((p for p in pages if p['page_name'] == page_name), None)
    
    if page_to_delete:
        # Excluir a imagem do Cloudinary
        cloudinary.uploader.destroy(page_to_delete['image_public_id'])
        
        # Remover a página da lista
        pages.remove(page_to_delete)
    
    return redirect(url_for('rotas.index'))
