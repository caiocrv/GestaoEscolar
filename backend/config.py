# Configuracoes (senha, usuario, rotas, entre outros)
import os
from dotenv import load_dotenv

# Carrega variaveis do .env
load_dotenv()

class Config:
    MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
    MYSQL_USER = os.getenv("MYSQL_USER", "admin")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
    MYSQL_DB = os.getenv("MYSQL_DB", "gestaoescolar")
    MYSQL_PORT = int(os.getenv("MYSQL_PORT", 3306))