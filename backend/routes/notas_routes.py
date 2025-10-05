from flask import Blueprint, jsonify
from utils.db_connection import get_conn
from services.media_service import calcular_media

notas_bp = Blueprint("nota", __name__)

@notas_bp.route("/media/<int:usuario_id>", methods=["GET"])
def media_aluno(usuario_id):
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT nota FROM notas_dos_alunos WHERE aluno_id = %s", (usuario_id,))
    notas = [float(row[0]) for row in cursor.fetchall()]
    cursor.close()
    conn.close()

    if not notas:
        return jsonify({"mensagem": "Aluno não possui notas"}), 404

    media = calcular_media(notas)
    return jsonify({
        "usuario_id": usuario_id,
        "notas": notas,
        "media": media
    })