from flask import Blueprint, render_template

from models import Cliente, servico

# Blueprint da home — sem url_prefix, então "/" é a raiz do site
dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    return render_template(
        "index.html",
        total_clientes=Cliente.query.count(),
        total_servicos=servico.query.count(),
        servicos_recentes=servico.listar_com_cliente()[:5],
    )
