from flask import Flask, render_template
from flask_cors import CORS
from utils.db_connection import init_pool

# importar blueprints das rotas
from routes.usuario_routes import usuarios_bp
from routes.turma_routes import turmas_bp
from routes.notas_routes import notas_bp
from routes.auth_routes import auth_bp

def create_app(config_object="config.Config"):
    # Iniciar o flask
    app = Flask(__name__, template_folder='../frontend', static_folder='../frontend')
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_object(config_object)
    app.config['JSON_SORT_KEYS'] = False
    app.config.from_object("config.Config")
    init_pool(app)

    # Registrar blueprints com prefixos
    app.register_blueprint(usuarios_bp, url_prefix="/api/usuarios")
    app.register_blueprint(turmas_bp, url_prefix="/api/turmas")
    app.register_blueprint(notas_bp, url_prefix="/api/notas")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    @app.route("/")
    def index():
        return render_template('index.html')
    
    @app.route("/login")
    def login():
        return render_template('login.html')
    
    @app.route("/register")
    def register():
        return render_template('register.html')
    
        

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='192.168.100.56', port=5000 , debug=True)
