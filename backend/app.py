import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

# Dossier où seront stockées les notes
NOTES_DIR = "notes"
os.makedirs(NOTES_DIR, exist_ok=True)

# Page principale
@app.route('/')
def home():
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    return render_template('index.html', files=files)

# API - Lister les notes
@app.route('/api/notes', methods=['GET'])
def list_notes():
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    return jsonify(files)

# API - Lire une note
@app.route('/note/<filename>', methods=['GET'])
def view_note_page(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(NOTES_DIR, filename)
    
    if not filename.endswith('.md') or not os.path.exists(filepath):
        return "Fichier non trouvé", 404
    
    files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.md')]
    return render_template('note.html', filename=filename, files=files)

@app.route('/api/note/<filename>', methods=['GET'])
def get_note_content(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(NOTES_DIR, filename)
    
    if not filename.endswith('.md') or not os.path.exists(filepath):
        return jsonify({"error": "Fichier non trouvé"}), 404
    
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return jsonify({"content": content})

# API - Enregistrer une note
@app.route('/api/note', methods=['POST'])
def save_note():
    data = request.json
    filename = secure_filename(data['filename'])
    
    if not filename.endswith('.md'):
        filename += '.md'
    
    content = data['content']
    
    filepath = os.path.join(NOTES_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return jsonify({"message": f"Note {filename} enregistrée avec succès !"})

# API - Supprimer une note
@app.route('/api/note/<filename>', methods=['DELETE'])
def delete_note(filename):
    filename = secure_filename(filename)
    filepath = os.path.join(NOTES_DIR, filename)
    
    if not filename.endswith('.md') or not os.path.exists(filepath):
        return jsonify({"error": "Fichier non trouvé"}), 404
    
    os.remove(filepath)
    return jsonify({"message": "Note supprimée"})

if __name__ == '__main__':
    app.run(debug=False)