from datetime import datetime

from . import db


class Operacao(db.Model):
    """Model — dados e acesso ao banco (tabela operacoes)."""

    __tablename__ = "operacoes"
    # insira as operações

    id = db.colum(db.Interger, primary_key = True)
    num1 = db.colum(db.Float, nullable = True) 
    num2 = db.colum(db.Float, nullable = False)
    operacao = db.colum(db.Interger, nullable = True)
    etapas = db.colum(db.Interger, nullable = True)
    resultado = db.colum(db.Interger, nullable = True)
    criado_em = db.colum(db.DateTime, default = datetime.now, nullable = True)

    @classmethod
    def salvar(cls, num1, num2, operacao, etapas, resultado, criado_em):
        registro = cls(
            num1=num1,
            num2=num2,
            operacao=operacao,
            etapas=etapas,
            resultado=str(resultado),
            criado_em=criado_em,
        )
        #insira os comandos par salvar
        
        db.session.add(registro)
        db.session.commit()
        return registro

    @classmethod
    def listar_recentes(cls, limite=10):
        return (
            cls.query.order_by(cls.criado_em.desc()).limit(limite).all()
        )

    def __repr__(self):
        return f"<Operacao {self.id}: {self.etapas}>"