# [ 📦 My Box ] - Gestion de Notes en Ligne

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/Backend-Flask-red)](https://flask.palletsprojects.com/)
[![HTML/CSS/JS](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-brightgreen)]()


## ❗ DOCUMENTATION IN OTHER LANGUAGES
📄 [English documentation](https://github.com/KucoDEV/MyBox/blob/main/README_en.md)


## ✨ Introduction

**[ 📦 My Box ]** est une application web permettant aux utilisateurs de créer, sauvegarder et consulter leurs notes en ligne. Ce projet est conçu pour offrir une expérience fluide et minimaliste avec un éditeur Markdown et une interface moderne.

## 🚀 Fonctionnalités

- 📄 **Création de notes** avec un éditeur Markdown interactif.
- 💾 **Sauvegarde automatique** des notes en ligne.
- 🔍 **Gestion des notes** via une interface simple et intuitive.
- ❌ **Suppression de notes** via une API REST.
- 🌐 **Interface responsive et moderne** avec Quill.js et un design en dark mode.

## 🛠️ Technologies Utilisées

### Backend
- [Flask](https://flask.palletsprojects.com/) - Framework web en Python
- [Flask-CORS](https://flask-cors.readthedocs.io/) - Gestion des requêtes cross-origin

### Frontend
- HTML5 / CSS3 / JavaScript
- [Quill.js](https://quilljs.com/) - Éditeur de texte enrichi
- JavaScript pour les interactions dynamiques

## 📂 Structure du Projet

```
📦 MyBox
├── backend/
│   ├── app.py             # Backend Flask
│   ├── static/
│   │   ├── script.js      # Scripts front-end
│   │   └── style.css      # Styles CSS
│   └── templates/
│       ├── index.html     # Page d'accueil avec liste des notes
│       └── note.html      # Page d'édition des notes
├── notes/
│   └── *.md               # Notes Markdown
├── README.md              # Documentation du projet
└── requirements.txt       # Liste des dépendances Python
```

## 📌 Installation et Configuration

### 1️⃣ Cloner le dépôt

```sh
git clone https://github.com/votre-repo/MyBox.git
cd MyBox
```

### 2️⃣ Installer les dépendances Python

Assurez-vous d'avoir Python installé, puis exécutez :

```sh
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application

Démarrer le serveur Flask :

```sh
python backend/app.py
```

L'application sera accessible sur **`http://127.0.0.1:5000/`**.

## 📡 API Endpoints

| Méthode | Endpoint             | Description |
|---------|----------------------|-------------|
| `GET`   | `/api/notes`         | Liste toutes les notes |
| `GET`   | `/api/note/<filename>` | Récupère le contenu d’une note |
| `POST`  | `/api/note`          | Enregistre une nouvelle note |
| `DELETE` | `/api/note/<filename>` | Supprime une note |

## 🎨 Interface Utilisateur

L'interface utilisateur de **[ 📦 My Box ]** est pensée pour être simple et efficace :
- 📜 **Liste des notes** affichées sous forme de menu latéral.
- ✍️ **Éditeur Markdown** interactif et facile à utiliser.
- 📌 **Bouton de sauvegarde** permettant d'enregistrer instantanément les notes.

## 📜 Licence

Ce projet est sous licence **MIT**. Vous êtes libre de le modifier et de l'utiliser comme bon vous semble.

---

✨ **Développé avec ❤️ par [KucoDEV](https://github.com/KucoDEV/)** ✨
