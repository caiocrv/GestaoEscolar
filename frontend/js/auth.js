const API_URL = "http://192.168.100.56:5000/api/auth/login"

document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formLogin");
    if (form) {
        form.addEventListener("submit", async (event) => {
            event.preventDefault();
            await realizarLogin();
        });
    }
});

async function realizarLogin() {
    console.log("Funcao login java script")
    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value.trim();

    if (!email || !senha) {
        alert("Preencha todos os campos!");
        return;
    }

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ email, senha })
        });

        const result = await response.json();

        if (response.ok) {
            alert("Login realizado com sucesso!");

            // Salvar token e informações do usuário
            localStorage.setItem("token", result.token);
            localStorage.setItem("usuario_nome", result.usuario.nome);
            localStorage.setItem("usuario_cargo", result.usuario.cargo);

            // Redirecionar com base no cargo
            const cargo = result.usuario.cargo.toLowerCase();
            if (cargo === "aluno") {
                console.log("Acesso aluno")
                window.location.href = "/home";
            } else if (cargo === "professor") {
                console.log("Acesso professor")
                window.location.href = "/home";
            } else if (cargo === "administrador") {
                console.log("Acesso admin")
                window.location.href = "/home";
            } else {
                alert("Cargo desconhecido. Contate o administrador.");
            }

        } else {
            alert(result.erro || "Email ou senha incorretos!");
        }
    } catch (error) {
        console.error("Erro ao conectar à API:", error);
        alert("Não foi possível conectar ao servidor. {auth java script}");
    }
}