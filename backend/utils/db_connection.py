from mysql.connector import pooling
from flask import current_app

_pool = None

def init_pool(app):
    global _pool

    _pool = pooling.MySQLConnectionPool(
        pool_name  = "mypool",
        pool_size = 5,
        host = app.config["MYSQL_HOST"],
        user = app.config["MYSQL_USER"],
        password = app.config["MYSQL_PASSWORD"],
        database = app.config["MYSQL_DB"],
        port = app.config.get("MYSQL_PORT", 3306)
    )

def get_conn():
    if _pool is None:
        raise RuntimeError("Pool não inicializado. Chame init_pool(app) no startup.")
    return _pool.get_connection()