const root = document.getElementById("root")

fetch("user_name.json")
    .then(response => response.json())
    .then(user_name => {
        user_name.forEach(i => {
            root.innerHTML += `
        <h1>Ishchi nomi: ${i.ishchi_nomi}</h1>
        <p>Ishchi joyi: ${i.ish_joyi}</p>
        <p>Ish vaqti: ${i.ish_vaqti}</p>
        <i>Daromadi: ${i.daromadi}</i>
        `;
        });
    });