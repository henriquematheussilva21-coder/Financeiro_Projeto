from database import get_session, criar_tabelas
from models.transacao import Transacao


class FinanceiroService:
    """Centraliza a regra de negócio do sistema desktop."""

    def __init__(self):
        criar_tabelas()

    def adicionar_transacao(self, tipo, descricao, valor, categoria):
        """Cria e persiste uma nova transação no banco."""
        session = get_session()
        nova = Transacao(tipo=tipo, descricao=descricao, valor=valor, categoria=categoria)
        session.add(nova)
        session.commit()
        session.close()

    def listar_transacoes(self):
        """Retorna todas as transações ordenadas pela mais recente."""
        session = get_session()
        resultado = session.query(Transacao).order_by(Transacao.id.desc()).all()
        session.close()
        return resultado

    def buscar_por_id(self, id):
        """Retorna uma transação pelo id."""
        session = get_session()
        resultado = session.get(Transacao, id)
        session.close()
        return resultado

    def editar_transacao(self, id, tipo, descricao, valor, categoria):
        """Atualiza os dados de uma transação existente."""
        session = get_session()
        transacao = session.get(Transacao, id)
        if not transacao:
            session.close()
            return None
        transacao.tipo = tipo
        transacao.descricao = descricao
        transacao.valor = valor
        transacao.categoria = categoria
        session.commit()
        session.close()

    def excluir_transacao(self, id):
        """Remove uma transação do banco."""
        session = get_session()
        transacao = session.get(Transacao, id)
        if not transacao:
            session.close()
            return False
        session.delete(transacao)
        session.commit()
        session.close()
        return True

    def calcular_saldo(self):
        """Retorna (total_receitas, total_despesas, saldo)."""
        transacoes = self.listar_transacoes()
        total_receitas = sum(t.valor for t in transacoes if t.tipo == "receita")
        total_despesas = sum(t.valor for t in transacoes if t.tipo == "despesa")
        saldo = total_receitas - total_despesas
        return total_receitas, total_despesas, saldo

    def filtrar_por_categoria(self, categoria):
        """Retorna transações de uma categoria específica."""
        session = get_session()
        resultado = session.query(Transacao).filter(
            Transacao.categoria.ilike(categoria)
        ).order_by(Transacao.id.desc()).all()
        session.close()
        return resultado

    def listar_categorias(self):
        """Retorna lista ordenada de categorias únicas."""
        session = get_session()
        resultado = session.query(Transacao.categoria).distinct().all()
        session.close()
        return sorted(r[0] for r in resultado)