from flask import Flask, request, jsonify, make_response
from utils.db_connection import get_conn, init_pool


def create_app(config_object="config.Config"):
        app = Flask(__name__)
        app.config.from_object(config_object)
        app.config['JSON_SORT_KEYS'] = False
        app.config.from_object("config.Config")
        init_pool(app)

        @app.route("/usuarios", methods=["GET"])
        def listar_usuarios():
                conn = get_conn()
                cursor = conn.cursor(dictionary=False)
                cursor.execute("SELECT id, nome, cargo FROM usuarios")
                rows = cursor.fetchall()
                cursor.close()
                conn.close()
                return make_response(
                       jsonify(rows)
                )
        

        @app.route("/debug-config")
        def debug_config():
               return jsonify ({
                        "MYSQL_HOST": app.config["MYSQL_HOST"],
                        "MYSQL_USER": app.config["MYSQL_USER"],
                        "MYSQL_PASSWORD": app.config["MYSQL_PASSWORD"],
                        "MYSQL_DB": app.config["MYSQL_DB"]
               })
        
        return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000 , debug=True)
