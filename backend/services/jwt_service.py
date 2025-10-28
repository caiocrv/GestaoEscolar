import jwt
from datetime import datetime, timedelta
from flask import current_app

def gerar_token (usuario_id, cargo):
    payload = {
        "usuario_id": usuario_id,
        "cargo": cargo,
        "exp": datetime.utcnow() + current_app.config["JWT_EXPIRATION"],
        "iat": datetime.utcnow()
    }
    token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
    return token

def verificar_token(token):
    try:
        payload = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None