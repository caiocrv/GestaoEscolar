from flask import Flask, request, jsonify, make_response
from utils.db_connection import get_conn, init_pool

# importar blueprints das rotas
from routes.usuario_routes import usuarios_bp

def create_app(config_object="config.Config"):
        # Iniciar o flask
        app = Flask(__name__)
        app.config.from_object(config_object)
        app.config['JSON_SORT_KEYS'] = False
        app.config.from_object("config.Config")
        init_pool(app)

        # Registrar blueprints com prefixos
        app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
        
        return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000 , debug=True)
