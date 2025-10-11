# Configuracoes (senha, usuario, tokens, entre outros)
import os
from dotenv import load_dotenv

# Carrega variaveis do .env
load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "")
    MYSQL_USER = os.getenv("MYSQL_USER", "")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))

    EMAIL_USERNAME = os.getenv("EMAIL_USERNAME", "luna.projetosenac@gmail.com")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "qtuu tkli ngfl lavm")