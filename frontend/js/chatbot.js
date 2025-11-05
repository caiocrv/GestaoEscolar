document.getElementById("send-btn").addEventListener("click", enviarMensagem);
document.getElementById("chat").addEventListener("keypress", function(e) {
    if (e.key === "Enter") enviarMensagem();
});

async function enviarMensagem() {
    const input = document.getElementById("chat");
    const texto = input.value.trim();
    const chatBox = document.getElementById("chat-messages");

    if (!texto) return;

    // Exibe mensagem do usuário
    chatBox.innerHTML += `<div class="msg-user">${texto}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;

    input.value = "";

    try {
        const response = await fetch("http://192.168.100.56:5000/api/chatbot/perguntar", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ mensagem: texto })
        });

        const data = await response.json();

        // Exibe resposta do chatbot
        chatBox.innerHTML += `<div class="msg-bot">${data.resposta}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;

    } catch (error) {
        chatBox.innerHTML += `<div class="msg-bot">⚠️ Erro ao conectar ao chatbot.</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
