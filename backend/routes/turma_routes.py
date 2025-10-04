from flask import Blueprint, make_response, jsonify, request
from utils.db_connection import get_conn

turmas_bp = Blueprint("turma", __name__)

@turmas_bp.route("/", methods=['GET'])
def listar_turmas():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM turmas")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(rows), 200
    )   

@turmas_bp.route("/", methods=['POST'])
def criar_turmas():
    dados = request.json
    nome_turma = dados.get("nome_turma")

    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO turmas (nome) VALUES (%s)", (nome_turma,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return make_response(jsonify({"mensagem": "Turma criada com sucesso"}), 201)
