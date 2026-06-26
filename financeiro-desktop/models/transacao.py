from datetime import datetime
from sqlalchemy import Column, Integer, String, Float
from database import Base


class Transacao(Base):
    """Representa uma receita ou despesa do sistema."""

    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    tipo = Column(String(10), nullable=False)
    descricao = Column(String(100), nullable=False)
    valor = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False)
    data = Column(String(10), nullable=False)

    def __init__(self, tipo, descricao, valor, categoria, data=None):
        self.tipo = tipo
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data if data else datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        sinal = "+" if self.tipo == "receita" else "-"
        return (
            f"[{self.id}] {self.data} | {self.tipo.upper():<8} | "
            f"{sinal}R$ {self.valor:.2f} | {self.categoria:<15} | {self.descricao}"
        )