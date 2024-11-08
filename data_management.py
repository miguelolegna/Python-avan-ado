import json
import os

json_file_path = 'images.json'

# Função para ler os dados das imagens
def read_images_data():
    if not os.path.exists(json_file_path):
        return []
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# Função para salvar os dados no JSON
def save_images_data(images_data):
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(images_data, f, ensure_ascii=False, indent=4)
