from . import db
from .base import ModeloBase


class servico(ModeloBase):
    """servico principal — pertence a um Cliente (chave estrangeira)."""

    __tablename__ = "servicos"

    cliente_id = db.Column(db.Integer, db.ForeignKey("clientes.id"), nullable=False)
    nome_do_cao = db.Column(db.String(30), nullable=False, default="pendente")
    raca = db.Column(db.String(30), nullable=False, default="pendente")
    peso_do_cao = db.Column(db.String(30), nullable=False, default="pendente")
    servicos = db.Column(db.String(30), nullable=False, default="pendente")
    status = db.Column(db.String(30), nullable=False, default="pendente")
    observacao = db.Column(db.String(255), nullable=True)
    valor_total = db.Column(db.String(30), nullable=False, default="pendente")

    cliente = db.relationship("Cliente", back_populates="servicos")
    itens = db.relationship(
        "ItemServico", back_populates="servico", cascade="all, delete-orphan"
    )

    # @property = "parece um atributo, mas calcula na hora"
    # Use: servico.total   (SEM parênteses) — no template fica {{ servico.total }}
    # Não guarda no banco; soma os itens toda vez que você pede.
    @property
    def total(self):
        return sum((item.servico * item.valor) + item.raca * iten.peso_do_cao for item in self.itens)

    @classmethod
    def listar_com_cliente(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()

    @classmethod
    def criar_com_itens(cls, cliente_id, itens_dados, observacao=""):
        servico = cls(
            cliente_id=cliente_id,
            observacao=observacao or None,
            status="pendente",
        )
        db.session.add(servico)
        db.session.flush()

        for item in itens_dados:
            db.session.add(
                ItemServico(
                    servico_id=servico.id,
                    produto=item["produto"],
                    quantidade=item["quantidade"],
                    preco_unitario=item["preco_unitario"],
                )
            )
        db.session.commit()
        return servico

    def __repr__(self):
        return f"<servico {self.id} cliente={self.cliente_id}>"


class ItemServico(ModeloBase):
    """Itens do servico — segunda tabela ligada a servico (FK)."""

    __tablename__ = "itens_servico"

    servico_id = db.Column(db.Integer, db.ForeignKey("servicos.id"), nullable=False)
    produto = db.Column(db.String(120), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    preco_unitario = db.Column(db.Float, nullable=False)

    servico = db.relationship("servico", back_populates="itens")

    # @property de novo: quantidade * preço, sem chamar subtotal()
    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def __repr__(self):
        return f"<ItemServico {self.produto} x{self.quantidade}>"
