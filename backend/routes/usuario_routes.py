from flask import Blueprint, make_response, jsonify, request
from utils.db_connection import get_conn
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
        senha = ph.hash(dados.get("senha"))
        cargo = dados.get("cargo")
        
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha, cargo) VALUES (%s, %s, %s, %s)", (nome, email, senha, cargo))
        conn.commit()
        cursor.close()
        conn.close()

        return make_response(jsonify({"mensagem": "Usuário criado com sucesso"}), 201)