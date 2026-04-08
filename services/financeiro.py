import json
import os
from models.transacao import Transacao

ARQUIVO_DADOS = "data/transacoes.json"


class FinanceiroService:
    """Centraliza a regra de negócio do sistema."""

    def __init__(self):
        self.transacoes = []
        self._garantir_pasta_data()
        self.carregar_dados()

    def _garantir_pasta_data(self):
        """Cria a pasta data se ela ainda não existir."""
        os.makedirs("data", exist_ok=True)

    def salvar_dados(self):
        """Salva as transações em JSON."""
        dados = [transacao.to_dict() for transacao in self.transacoes]

        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    def carregar_dados(self):
        """Carrega o conteúdo do JSON, caso ele já exista."""
        if not os.path.exists(ARQUIVO_DADOS):
            return

        with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
            try:
                dados = json.load(arquivo)
                self.transacoes = [Transacao.from_dict(item) for item in dados]
            except json.JSONDecodeError:
                # Preferi não quebrar o programa se o JSON vier vazio ou corrompido.
                self.transacoes = []

    def _proximo_id(self):
        """Gera o próximo id da lista."""
        if not self.transacoes:
            return 1

        return max(transacao.id for transacao in self.transacoes) + 1

    def adicionar_transacao(self, tipo, descricao, valor, categoria):
        nova_transacao = Transacao(
            id=self._proximo_id(),
            tipo=tipo,
            descricao=descricao,
            valor=valor,
            categoria=categoria
        )
        self.transacoes.append(nova_transacao)
        self.salvar_dados()
        return nova_transacao

    def listar_transacoes(self):
        return self.transacoes
    
    def calcular_saldo(self):
        total_receitas = sum(item.valor for item in self.transacoes if item.tipo == "receita")
        total_despesas = sum(item.valor for item in self.transacoes if item.tipo == "despesa")
        saldo = total_receitas - total_despesas
        return total_receitas, total_despesas, saldo
    
    def filtrar_por_categoria(self, categoria):
        categoria = categoria.lower()
        return [t for t in self.transacoes if t.categoria.lower() == categoria]
    
    def listar_categorias(self):
        return sorted(set(t.categoria for t in self.transacoes))