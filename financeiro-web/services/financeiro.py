from database import db
from models.transacao import Transacao


class FinanceiroService:
    """Centraliza a regra de negócio do sistema."""

    def adicionar_transacao(self, tipo, descricao, valor, categoria):
        """Cria e persiste uma nova transação no banco."""
        nova = Transacao(
            tipo=tipo,
            descricao=descricao,
            valor=valor,
            categoria=categoria,
        )
        db.session.add(nova)
        db.session.commit()
        return nova

    def listar_transacoes(self):
        """Retorna todas as transações ordenadas pela mais recente."""
        return Transacao.query.order_by(Transacao.id.desc()).all()

    def buscar_por_id(self, id):
        """Retorna uma transação pelo id ou None se não existir."""
        return Transacao.query.get(id)

    def editar_transacao(self, id, tipo, descricao, valor, categoria):
        """Atualiza os dados de uma transação existente."""
        transacao = self.buscar_por_id(id)
        if not transacao:
            return None
        transacao.tipo = tipo
        transacao.descricao = descricao
        transacao.valor = valor
        transacao.categoria = categoria
        db.session.commit()
        return transacao

    def excluir_transacao(self, id):
        """Remove uma transação do banco."""
        transacao = self.buscar_por_id(id)
        if not transacao:
            return False
        db.session.delete(transacao)
        db.session.commit()
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
        return Transacao.query.filter(
            Transacao.categoria.ilike(categoria)
        ).order_by(Transacao.id.desc()).all()

    def listar_categorias(self):
        """Retorna lista ordenada de categorias únicas já utilizadas."""
        resultado = db.session.query(Transacao.categoria).distinct().all()
        return sorted(r[0] for r in resultado)

    def resumo_por_categoria(self):
        """Retorna dict {categoria: total} para o gráfico do dashboard."""
        transacoes = self.listar_transacoes()
        resumo = {}
        for t in transacoes:
            resumo[t.categoria] = resumo.get(t.categoria, 0) + t.valor
        return resumo