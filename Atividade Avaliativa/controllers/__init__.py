# Esta pasta controllers/ exporta os Blueprints para o app.py registrar.
# Cada arquivo *_controller.py cria um Blueprint com nome único (ex: "clientes").
from .clientes_controller import clientes_bp
from .dashboard_controller import dashboard_bp
from .servicos_controller import servicos_bp

__all__ = ["dashboard_bp", "clientes_bp", "servicos_bp"]