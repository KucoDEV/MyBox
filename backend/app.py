import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

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
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        files = [f for f in os.listdir(NOTES_DIR) if f.endswith('.md')]
        return render_template('note.html', filename=filename, files=files)
    return "Fichier non trouvé", 404

@app.route('/api/note/<filename>', methods=['GET'])
def get_note_content(filename):
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
        return jsonify({"content": content})
    return jsonify({"error": "Fichier non trouvé"}), 404


# API - Enregistrer une note
@app.route('/api/note', methods=['POST'])
def save_note():
    data = request.json
    filename = data['filename']

    if not filename.endswith('.md'):
        filename += '.md'

    content = data['content']
    
    notes_directory = 'notes'
    if not os.path.exists(notes_directory):
        os.makedirs(notes_directory)

    with open(os.path.join(notes_directory, filename), 'w', encoding='utf-8') as f:
        f.write(content)

    return jsonify({"message": f"Note {filename} enregistrée avec succès !"})


# API - Supprimer une note
@app.route('/api/note/<filename>', methods=['DELETE'])
def delete_note(filename):
    filepath = os.path.join(NOTES_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return jsonify({"message": "Note supprimée"})
    return jsonify({"error": "Fichier non trouvé"}), 404

if __name__ == '__main__':
    app.run(debug=True)