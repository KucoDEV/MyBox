# [ 📦 My Box ] - Online Notes Management

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Flask](https://img.shields.io/badge/Backend-Flask-red)](https://flask.palletsprojects.com/)
[![HTML/CSS/JS](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-brightgreen)]()

## ✨ Introduction

**[ 📦 My Box ]** is a web application that allows users to create, save, and view their notes online. This project is designed to provide a smooth and minimalist experience with a Markdown editor and a modern interface.

## 🚀 Features

- 📄 **Create notes** with an interactive Markdown editor.
- 💾 **Automatic saving** of notes online.
- 🔍 **Manage notes** via a simple and intuitive interface.
- ❌ **Delete notes** via a REST API.
- 🌐 **Responsive and modern interface** with Quill.js and a dark mode design.

## 🛠️ Technologies Used

### Backend
- [Flask](https://flask.palletsprojects.com/) - Python web framework
- [Flask-CORS](https://flask-cors.readthedocs.io/) - Handling cross-origin requests

### Frontend
- HTML5 / CSS3 / JavaScript
- [Quill.js](https://quilljs.com/) - Rich text editor
- JavaScript for dynamic interactions

## 📂 Project Structure

```
📦 MyBox
├── backend/
│   ├── app.py             # Flask backend
│   ├── static/
│   │   ├── script.js      # Frontend scripts
│   │   └── style.css      # CSS styles
│   └── templates/
│       ├── index.html     # Homepage with note list
│       └── note.html      # Note editing page
├── notes/
│   └── *.md               # Markdown notes
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies list
```

## 📌 Installation and Setup

### 1️⃣ Clone the repository

```sh
git clone https://github.com/your-repo/MyBox.git
cd MyBox
```

### 2️⃣ Install Python dependencies

Make sure Python is installed, then run:

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the application

Start the Flask server:

```sh
python backend/app.py
```

The application will be accessible at **`http://127.0.0.1:5000/`**.

## 📡 API Endpoints

| Method  | Endpoint              | Description |
|---------|----------------------|-------------|
| `GET`   | `/api/notes`         | Lists all notes |
| `GET`   | `/api/note/<filename>` | Retrieves the content of a note |
| `POST`  | `/api/note`          | Saves a new note |
| `DELETE` | `/api/note/<filename>` | Deletes a note |

## 🎨 User Interface

The user interface of **[ 📦 My Box ]** is designed to be simple and efficient:
- 📜 **List of notes** displayed as a sidebar menu.
- ✍️ **Interactive Markdown editor** for easy note-taking.
- 📌 **Save button** to instantly save notes.

## 📜 License

This project is licensed under the **MIT** license. You are free to modify and use it as you see fit.

---

✨ **Developed with ❤️ by [KucoDEV](https://github.com/KucoDEV/)** ✨
