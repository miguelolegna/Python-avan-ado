from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from data_management import read_images_data, save_images_data
from utils import create_html_file
import os
from flask import current_app

rotas = Blueprint('rotas', __name__)

# Função para criar uma nova página
def create_new_page_with_image(page_name, image_file):
    image_filename = secure_filename(image_file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    image_file.save(os.path.join(upload_folder, image_filename))

    # Carrega os dados antigos do arquivo JSON
    images_data = read_images_data()

    # Adiciona uma nova entrada para a imagem
    new_image_entry = {
        "page_name": page_name,
        "image_filename": image_filename,
        "image_path": os.path.join(upload_folder, image_filename) 
    }
    images_data.append(new_image_entry)

    # Salva as alterações no arquivo JSON
    save_images_data(images_data)

    return new_image_entry

@rotas.route('/')
def index():
    images_data = read_images_data()
    return render_template('index.html', images_data=images_data)

@rotas.route('/create_page', methods=['POST', 'GET'])
def create_page():
    if request.method == 'POST':
        page_name = request.form['page_name']
        image_file = request.files.get('image')

        if not image_file:
            return "Erro: Nenhuma imagem selecionada", 400

        # Cria a nova página e salva a imagem no JSON
        new_image_entry = create_new_page_with_image(page_name, image_file)

        # Cria o HTML da nova página
        create_html_file(new_image_entry["image_filename"], new_image_entry["page_name"])

        return render_template('new_page.html', page=new_image_entry)

    return render_template("create_page_form.html")
