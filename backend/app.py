from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autoriser les requêtes du frontend

# Configuration de la base de données SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modèle de données pour les notes
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

# Créer la base de données
with app.app_context():
    db.create_all()

# Route pour afficher l'interface utilisateur
@app.route('/')
def home():
    return render_template('index.html')

# API pour récupérer les notes
@app.route('/api/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([{"id": note.id, "content": note.content} for note in notes])

# API pour ajouter une note
@app.route('/api/notes', methods=['POST'])
def add_note():
    data = request.json
    new_note = Note(content=data['content'])
    db.session.add(new_note)
    db.session.commit()
    return jsonify({"message": "Note ajoutée !"})

# API pour supprimer une note
@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note:
        db.session.delete(note)
        db.session.commit()
        return jsonify({"message": "Note supprimée"})
    return jsonify({"message": "Note non trouvée"}), 404

if __name__ == '__main__':
    app.run(debug=True)
