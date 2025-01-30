var quill = new Quill('#editor', { theme: 'snow' });

// Fonction pour sauvegarder une note
function saveNote() {
    let filename = document.getElementById("filename").value;
    let content = quill.root.innerHTML;

    fetch('/api/note', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ filename, content })
    })
    .then(() => location.reload());
}

// Fonction pour supprimer une note
function deleteNote(filename) {
    fetch(`/api/note/${filename}`, { method: 'DELETE' })
    .then(() => location.reload());
}
