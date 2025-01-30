document.addEventListener("DOMContentLoaded", function () {
    loadNotes();
});

// Charger la liste des notes
function loadNotes() {
    fetch("/api/notes")
        .then(response => response.json())
        .then(files => {
            let noteList = document.getElementById("note-list");
            noteList.innerHTML = "";
            files.forEach(file => {
                let listItem = document.createElement("li");
                let link = document.createElement("a");
                link.href = `/note/${file}`;
                link.textContent = file;
                listItem.appendChild(link);
                noteList.appendChild(listItem);
            });
        });
}

// Sauvegarder une note
function saveNote() {
    let filename = document.getElementById("filename").value.trim();
    let content = quill.root.innerHTML;
    if (filename === "") {
        alert("Veuillez entrer un nom de fichier !");
        return;
    }

    fetch("/api/note", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ filename, content })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadNotes(); // Recharger la liste
    });
}

// Supprimer une note
function deleteNote(filename) {
    if (confirm("Voulez-vous vraiment supprimer cette note ?")) {
        fetch(`/api/note/${filename}`, { method: "DELETE" })
            .then(response => response.json())
            .then(data => {
                alert(data.message);
                loadNotes();
            });
    }
}

var quill = new Quill("#editor", {
    theme: "snow",
    modules: {
        toolbar: "#toolbar"
    }
});

function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const container = document.getElementById("main-container");
    sidebar.classList.toggle("closed");
    container.classList.toggle("menu-closed");
}