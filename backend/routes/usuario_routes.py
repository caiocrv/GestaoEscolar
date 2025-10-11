from flask import Blueprint, make_response, jsonify, request
from utils.db_connection import get_conn
from utils.email_service import enviar_email
from argon2 import PasswordHasher

usuarios_bp = Blueprint("usuario", __name__)

ph = PasswordHasher()

@usuarios_bp.route("/", methods=['GET'])
def listar_usuarios():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, email, senha, cargo FROM usuarios")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return make_response(
        jsonify(rows), 200
    )

@usuarios_bp.route("/", methods=['POST'])
def criar_usuarios():
    dados = request.json
    nome = dados.get("nome")
    email = dados.get("email")
    email_institucional = dados.get("email_institucional")
    senha = ph.hash(dados.get("senha"))
    cargo = "aluno"
    print("")
    print(email)
    print(email_institucional)
    print("")
    
    # Valida se o nome esta composto
    partes = nome.strip().split()
    if len(partes) < 2:
        return jsonify({"erro": "Informe nome e sobrenome"}), 400
    
    email_institucional = f"{email_institucional}@gestaoescolar.com.br"

    conn = get_conn()
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, senha, cargo) VALUES (%s, %s, %s, %s)", (nome, email_institucional, senha, cargo))
        conn.commit()
    except Exception as e:
        conn.rollback()
        return make_response(jsonify({"erro": str(e)}), 500)
    finally:
        cursor.close()
        conn.close()

    print("")
    print(email)
    print(email_institucional)
    print("")
    enviar_email(nome, email, email_institucional)

    return make_response(jsonify({"mensagem": "Usuário criado com sucesso"}), 201)