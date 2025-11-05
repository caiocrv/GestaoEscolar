from flask import Blueprint, jsonify, request, current_app
from utils.db_connection import get_conn
from services.media_service import calcular_media
from routes.auth_routes import auth_required
import jwt

notas_bp = Blueprint("nota", __name__)

@notas_bp.route("/minhas", methods=["GET"])
@auth_required
def minhas_notas():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")

    if not token:
        return jsonify({"erro": "Token não enviado"}), 401

    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        usuario_id = payload["usuario_id"]

        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT nota FROM notas_dos_alunos WHERE aluno_id = %s", (usuario_id,))
        notas = [float(row[0]) for row in cursor.fetchall()]
        cursor.close()
        conn.close()

        if not notas:
            return jsonify({"mensagem": "Você ainda não possui notas"}), 404

        media = calcular_media(notas)

        return jsonify({
            "usuario_id": usuario_id,
            "notas": notas,
            "media": media
        }), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"erro": "Sessão expirada"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"erro": "Token inválido"}), 401
