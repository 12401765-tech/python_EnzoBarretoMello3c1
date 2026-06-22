import os

from flask import Flask

# Cada "bp" importado é um Blueprint — um pacote de rotas (clientes, servicos, etc.)
from controllers.clientes_controller import clientes_bp
from controllers.dashboard_controller import dashboard_bp
from controllers.servicos_controller import servicos_bp
from models import Cliente, ItemServico, servico, db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "servicos.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # BLUEPRINT — explicação rápida:
    # Em vez de jogar TODAS as rotas aqui no app.py, cada assunto fica no seu controller.
    # register_blueprint = "liga" esse pacote de rotas ao Flask (tipo plugar um módulo no jogo).
    # clientes_bp → URLs começam com /clientes
    # servicos_bp  → URLs começam com /servicos
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(servicos_bp)


    with app.app_context():
        db.create_all()

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
