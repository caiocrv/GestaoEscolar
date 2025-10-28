from flask import Blueprint, request, jsonify, make_response
from utils.db_connection import get_conn
from argon2 import PasswordHasher
from services.jwt_service import gerar_token

auth_bp = Blueprint("login", __name__)
ph = PasswordHasher()

@auth_bp.route("/login", methods=["POST"])
def login():
    print("Entrou na rota login")
    dados = request.json
    email = dados.get("email")
    senha = dados.get("senha")

    conn = get_conn()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, nome, email, senha, cargo FROM usuarios WHERE email = %s", (email, ))
    usuario = cursor.fetchone()
    print(usuario)
    cursor.close()
    conn.close()

    if not usuario:
        return make_response(jsonify({"erro": "Usuário não encontrado"}), 404)
    
    try:
        ph.verify(usuario["senha"], senha)
    except Exception:
        return make_response(jsonify({"erro": "Senha incorreta"}), 401)
    
    token = gerar_token(usuario["id"], usuario["cargo"])
    print(token)
    return jsonify({
        "mensagem": "Login realizado com sucesso",
        "token": token,
        "usuario": {
            "id": usuario["id"],
            "nome": usuario["nome"],
            "email": usuario["email"],
            "cargo": usuario["cargo"]
        }
    })