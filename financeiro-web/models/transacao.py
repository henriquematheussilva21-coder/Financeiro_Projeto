from datetime import datetime
from database import db


class Transacao(db.Model):
    """Representa uma receita ou despesa do sistema."""

    __tablename__ = "transacoes"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(10), nullable=False)
    descricao = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    data = db.Column(db.String(10), nullable=False)

    def __init__(self, tipo, descricao, valor, categoria, data=None):
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data if data else datetime.now().strftime("%d/%m/%Y")

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "descricao": self.descricao,
            "valor": self.valor,
            "categoria": self.categoria,
            "data": self.data,
        }

    def __str__(self):
        sinal = "+" if self.tipo == "receita" else "-"
        return (
            f"[{self.id}] {self.data} | {self.tipo.upper():<8} | "
            f"{sinal}R$ {self.valor:.2f} | {self.categoria:<15} | {self.descricao}"
        )