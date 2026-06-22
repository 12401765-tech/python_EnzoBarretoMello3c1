from flask import Blueprint, redirect, render_template, request, url_for

from models import Cliente, servico, db

# Outro Blueprint, outro "módulo" de rotas — mesmo app, pasta mental separada (servicos)
# No HTML: url_for('servicos.listar') — primeiro nome é o Blueprint, segundo é a função
servicos_bp = Blueprint("servicos", __name__, url_prefix="/servicos")

def _ler_itens_form():
    servicos = request.form.getlist("servicos")
    quantidades = request.form.getlist("quantidade")
    precos = request.form.getlist("preco_unitario")
    itens = []
    for servicos, qtd, preco in zip(servicos, quantidades, precos):
        servicos = servicos.strip()
        if not servicos:
            continue
        try:
            itens.append(
                {
                    "servicos": servicos,
                    "quantidade": int(qtd),
                    "preco_unitario": float(str(preco).replace(",", ".")),
                }
            )
        except ValueError:
            return None, "Quantidade ou preço inválido nos itens."
    if not itens:
        return None, "Adicione pelo menos um item ao pedido."
    return itens, None


def calcular_valor_total():
    quantidades = request.form.getlist("quantidade")
    


# Decorator @route: GET em /servicos/ chama esta função
@servicos_bp.route("/")
def listar():
    return render_template(
        "servicos/lista.html", servicos=servico.listar_com_cliente()
    )


@servicos_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    clientes = Cliente.listar_ordenados()
    if not clientes:
        return render_template(
            "servicos/formulario.html",
            titulo="Novo pedido",
            clientes=[],
            erro="Cadastre um cliente antes de criar servicos.",
        )

    if request.method == "POST":
        try:
            cliente_id = int(request.form.get("cliente_id", 0))
        except ValueError:
            cliente_id = 0
        observacao = request.form.get("observacao", "").strip()
        itens, erro_itens = _ler_itens_form()

        if not cliente_id or not db.session.get(Cliente, cliente_id):
            erro = "Selecione um cliente válido."
        elif erro_itens:
            erro = erro_itens
        else:
            # @classmethod — monta pedido + itens num lugar só
            Pedido.criar_com_itens(cliente_id, itens, observacao)
            return redirect(url_for("servicos.listar"))
        return render_template(
            "servicos/formulario.html",
            titulo="Novo pedido",
            clientes=clientes,
            erro=erro,
            observacao=observacao,
        )

    return render_template(
        "servicos/formulario.html", titulo="Novo pedido", clientes=clientes
    )


@servicos_bp.route("/<int:pedido_id>")
def detalhe(pedido_id):
    pedido = db.session.get(Pedido, pedido_id)
    if not pedido:
        return redirect(url_for("servicos.listar"))
    return render_template("servicos/detalhe.html", pedido=pedido)
