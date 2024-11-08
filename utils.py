import os

# Função para criar o arquivo HTML dinâmico
def create_html_file(image_filename, page_name):
    template_dir = 'templates'
    file_path = os.path.join(template_dir, f'{page_name.lower()}.html')

    # Cria o diretório "templates" se não existir
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)

    # Cria o arquivo HTML se ele não existir
    if not os.path.isfile(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            content = f"""
            <html>
            <head>
                <title>{page_name}</title>
            </head>
            <body>
                <h1>Bem-vindo à página {page_name}!</h1>
                <p>Esta é a página {page_name}.</p>
                <img src="{{{{ url_for('static', filename='uploads/{image_filename}') }}}}" alt="{page_name}">
            </body>
            </html>
            """
            f.write(content)
