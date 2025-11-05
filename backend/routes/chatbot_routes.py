from flask import Blueprint, request, jsonify
from services.chatbot_service import enviar_mensagem_gemini

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/perguntar", methods=["POST"])
def perguntar():
    data = request.json
    msg = data.get("mensagem")

    try:
        resposta = enviar_mensagem_gemini(msg)
        return jsonify({"resposta": resposta})
    except Exception as e:
        print("Erro no chatbot:", e)
        return jsonify({"resposta": "Desculpe, houve um problema ao gerar a resposta."}), 500
