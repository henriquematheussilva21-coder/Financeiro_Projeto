from datetime import datetime

class Transacao:
    "Representa uma receita ou despesa do sistema"

    def __init__(self, id, tipo, descricao, valor, categoria, data=None):
        self.id = id
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
    
    @staticmethod
    def from_dict(dados):
        return Transacao(
            id=dados["id"],
            tipo=dados["tipo"],
            descricao=dados["descricao"],
            valor=dados["valor"],
            categoria=dados["categoria"],
            data=dados["data"],
        )
    
    def __str__(self):
        sinal = "+" if self.tipo == "receita" else "-" 
        return (
            f"[{self.id}] {self.data} | {self.tipo.upper():<8} | "
            f"{sinal}R$ {self.valor:.2f} | {self.categoria:<15} | {self.descricao}"
        )