const API_URL = "http://192.168.100.56:5000/api/usuarios/";

document.addEventListener("DOMContentLoaded", function() {
    const formCadastro = document.getElementById("formCadastro");
    formCadastro.addEventListener("submit", function(event) {
        event.preventDefault();
        cadastrarUsuario();
    });
});

async function cadastrarUsuario() {
    const nome = document.getElementById("nome").value;
    const senha = document.getElementById("password").value;
    const confirmaSenha = document.getElementById("confirmPassword").value;
    const email = document.getElementById("email").value;

    const primeiroNome = document.getElementById("nome").value.split(" ")[0];
    const ultimoNome = document.getElementById("nome").value.split(" ").slice(-1)[0];
    const email_institucional = `${primeiroNome.toLowerCase()}.${ultimoNome.toLowerCase()}`;

    if (!nome || !email || !senha || !confirmaSenha) {
        alert ("Preencha todos os campos");
        return;
    }

    let caractereEspecial = 0;
    let caractereMaiusculo = 0;

    if (senha !== confirmaSenha) {
        alert("As senhas não coincidem.");
        return;
    }

    for (let i = 0; i < senha.length; i++) {
        const caractere = senha[i];

        if (caractere == ' ') {
            alert("A senha não pode conter espaços.");
            return;
        }

        if ("@#?!&$".includes(caractere)) {
            caractereEspecial++;
        }

        if (caractere === caractere.toUpperCase() && caractere !== caractere.toLowerCase()) {
            caractereMaiusculo++;
        }
    }

    if (caractereEspecial === 0) {
        alert("A senha deve conter pelo menos um caractere especial (@, #, ?, !, & ou $).");
        return;
    }

    if (caractereMaiusculo === 0) {
        alert("A senha deve conter pelo menos uma letra maiúscula.");
        return;
    }

    const data = { nome, email, senha ,email_institucional};
    
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            alert(result.mensagem || "Usuário cadastrado com sucesso!");
            document.getElementById("formCadastro").reset();
        } else {
            alert(result.erro || "Erro ao cadastrar usuário!");
        }
    } catch (error) {
        console.error("Erro de conexão:", error);
        alert("Não foi possível conectar à API.");
    }
}