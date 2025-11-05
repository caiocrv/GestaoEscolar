import google.generativeai as genai
from flask import current_app

# Histórico curto da conversa (máx. 5 interações)
conversation_history = []

def enviar_mensagem_gemini(mensagem_do_usuario):
    # Pega a API Key direto do Flask
    api_key = current_app.config.get("GEMINI_API_KEY")
    system_prompt = current_app.config.get("SYSTEM_PROMPT", "")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=system_prompt
    )

    # Salva mensagem do usuário no histórico
    conversation_history.append({"role": "user", "parts": [mensagem_do_usuario]})
    if len(conversation_history) > 5:
        conversation_history.pop(0)

    try:
        resposta = model.generate_content(conversation_history)

        texto = resposta.text.strip()

        # Salva resposta no histórico
        conversation_history.append({"role": "model", "parts": [texto]})
        if len(conversation_history) > 5:
            conversation_history.pop(0)

        return texto

    except Exception as e:
        import traceback
        print("\n===== ERRO GEMINI =====")
        print(traceback.format_exc())
        print("===== FIM DO ERRO =====\n")
        return "Desculpe, ocorreu um erro interno. Já estou verificando! 🙂"

