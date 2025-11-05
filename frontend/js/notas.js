document.addEventListener("DOMContentLoaded", carregarNotas);

async function carregarNotas() {
    const token = localStorage.getItem("token");
    if (!token) {
        window.location.href = "/login";
        return;
    }

    try {
        const response = await fetch("http://192.168.100.56:5000/api/notas/minhas", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const dados = await response.json();
        console.log("Notas recebidas:", dados);

        const tabela = document.querySelector("table");

        tabela.innerHTML = "<tr><th>Atividade</th><th>Nota</th></tr>"; // limpa antes

        dados.forEach(nota => {
            tabela.innerHTML += `
                <tr>
                    <td>${nota.atividade}</td>
                    <td>${nota.nota}</td>
                </tr>
            `;
        });

    } catch (error) {
        console.error("Erro ao buscar notas:", error);
        alert("Erro ao buscar suas notas.");
    }
}
