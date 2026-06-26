import tkinter as tk
from tkinter import ttk, messagebox
from services.financeiro import FinanceiroService
from utils.validacoes import (
    validar_tipo, validar_valor, validar_descricao,
    validar_categoria, CATEGORIAS_PADRAO
)

service = FinanceiroService()


# ------------------
# JANELA PRINCIPAL
# ------------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("💰 Controle Financeiro")
        self.geometry("900x600")
        self.resizable(True, True)
        self.configure(bg="#f4f6f9")
        self._build_navbar()
        self._build_content()
        self.mostrar_dashboard()

    def _build_navbar(self):
        nav = tk.Frame(self, bg="#ffffff", height=50)
        nav.pack(fill="x", side="top")
        nav.pack_propagate(False)

        tk.Label(nav, text="💰 Financeiro", bg="#ffffff",
                 font=("Segoe UI", 13, "bold"), fg="#1e293b").pack(side="left", padx=20)

        tk.Button(nav, text="Dashboard", bg="#ffffff", fg="#6366f1",
                  font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2",
                  command=self.mostrar_dashboard).pack(side="left", padx=10)

        tk.Button(nav, text="Transações", bg="#ffffff", fg="#64748b",
                  font=("Segoe UI", 10), bd=0, cursor="hand2",
                  command=self.mostrar_transacoes).pack(side="left", padx=10)

        tk.Button(nav, text="+ Nova", bg="#6366f1", fg="#ffffff",
                  font=("Segoe UI", 10, "bold"), bd=0, cursor="hand2",
                  padx=12, pady=6,
                  command=self.abrir_form_nova).pack(side="right", padx=20)

    def _build_content(self):
        self.content = tk.Frame(self, bg="#f4f6f9")
        self.content.pack(fill="both", expand=True, padx=20, pady=20)

    def _limpar_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    # ----- Dashboard -----
    def mostrar_dashboard(self):
        self._limpar_content()
        receitas, despesas, saldo = service.calcular_saldo()

        # Título
        tk.Label(self.content, text="Dashboard", bg="#f4f6f9",
                 font=("Segoe UI", 16, "bold"), fg="#1e293b").pack(anchor="w", pady=(0, 15))

        # Cards
        cards_frame = tk.Frame(self.content, bg="#f4f6f9")
        cards_frame.pack(fill="x", pady=(0, 20))

        self._card(cards_frame, "RECEITAS", f"R$ {receitas:.2f}", "#22c55e").pack(side="left", padx=(0, 10))
        self._card(cards_frame, "DESPESAS", f"R$ {despesas:.2f}", "#ef4444").pack(side="left", padx=(0, 10))
        cor_saldo = "#6366f1" if saldo >= 0 else "#ef4444"
        self._card(cards_frame, "SALDO ATUAL", f"R$ {saldo:.2f}", cor_saldo).pack(side="left")

        # Últimas transações
        tk.Label(self.content, text="Últimas transações", bg="#f4f6f9",
                 font=("Segoe UI", 12, "bold"), fg="#1e293b").pack(anchor="w", pady=(0, 8))

        self._tabela(self.content, service.listar_transacoes()[:5], compacta=True)

    def _card(self, parent, label, valor, cor):
        frame = tk.Frame(parent, bg="#ffffff", relief="flat", bd=0)
        frame.configure(highlightbackground=cor, highlightthickness=3)
        tk.Label(frame, text=label, bg="#ffffff", fg="#64748b",
                 font=("Segoe UI", 8, "bold")).pack(anchor="w", padx=15, pady=(12, 0))
        tk.Label(frame, text=valor, bg="#ffffff", fg=cor,
                 font=("Segoe UI", 18, "bold")).pack(anchor="w", padx=15, pady=(0, 12))
        return frame

    # ----- Listagem -----
    def mostrar_transacoes(self, categoria_filtro=""):
        self._limpar_content()

        tk.Label(self.content, text="Transações", bg="#f4f6f9",
                 font=("Segoe UI", 16, "bold"), fg="#1e293b").pack(anchor="w", pady=(0, 10))

        # Filtro
        filtro_frame = tk.Frame(self.content, bg="#f4f6f9")
        filtro_frame.pack(fill="x", pady=(0, 10))

        tk.Label(filtro_frame, text="Filtrar por categoria:", bg="#f4f6f9",
                 font=("Segoe UI", 10)).pack(side="left", padx=(0, 8))

        categorias = ["Todas"] + service.listar_categorias()
        self.cat_var = tk.StringVar(value=categoria_filtro if categoria_filtro else "Todas")
        combo = ttk.Combobox(filtro_frame, textvariable=self.cat_var,
                             values=categorias, state="readonly", width=20)
        combo.pack(side="left")
        combo.bind("<<ComboboxSelected>>", lambda e: self._aplicar_filtro())

        # Tabela
        transacoes = (service.filtrar_por_categoria(categoria_filtro)
                      if categoria_filtro else service.listar_transacoes())
        self._tabela(self.content, transacoes, compacta=False)

    def _aplicar_filtro(self):
        cat = self.cat_var.get()
        self.mostrar_transacoes("" if cat == "Todas" else cat)

    def _tabela(self, parent, transacoes, compacta=False):
        frame = tk.Frame(parent, bg="#ffffff")
        frame.pack(fill="both", expand=True)

        colunas = ("id", "data", "tipo", "descricao", "categoria", "valor")
        tree = ttk.Treeview(frame, columns=colunas, show="headings",
                            height=5 if compacta else 15)

        tree.heading("id", text="#")
        tree.heading("data", text="Data")
        tree.heading("tipo", text="Tipo")
        tree.heading("descricao", text="Descrição")
        tree.heading("categoria", text="Categoria")
        tree.heading("valor", text="Valor")

        tree.column("id", width=40, anchor="center")
        tree.column("data", width=90, anchor="center")
        tree.column("tipo", width=80, anchor="center")
        tree.column("descricao", width=220)
        tree.column("categoria", width=120)
        tree.column("valor", width=100, anchor="e")

        for t in transacoes:
            sinal = "+" if t.tipo == "receita" else "-"
            tree.insert("", "end", iid=t.id, values=(
                t.id, t.data, t.tipo.upper(),
                t.descricao, t.categoria,
                f"{sinal} R$ {t.valor:.2f}"
            ))

        scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        if not compacta:
            btn_frame = tk.Frame(parent, bg="#f4f6f9")
            btn_frame.pack(fill="x", pady=8)

            tk.Button(btn_frame, text="✏️ Editar", bg="#6366f1", fg="white",
                      font=("Segoe UI", 10, "bold"), bd=0, padx=12, pady=6,
                      cursor="hand2",
                      command=lambda: self._editar_selecionado(tree)).pack(side="left", padx=(0, 8))

            tk.Button(btn_frame, text="🗑️ Excluir", bg="#ef4444", fg="white",
                      font=("Segoe UI", 10, "bold"), bd=0, padx=12, pady=6,
                      cursor="hand2",
                      command=lambda: self._excluir_selecionado(tree)).pack(side="left")

    def _editar_selecionado(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma transação para editar.")
            return
        id_selecionado = int(selecionado[0])
        transacao = service.buscar_por_id(id_selecionado)
        if transacao:
            self.abrir_form_editar(transacao)

    def _excluir_selecionado(self, tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showwarning("Atenção", "Selecione uma transação para excluir.")
            return
        id_selecionado = int(selecionado[0])
        confirmar = messagebox.askyesno("Confirmar", "Deseja excluir esta transação?")
        if confirmar:
            service.excluir_transacao(id_selecionado)
            messagebox.showinfo("Sucesso", "Transação excluída com sucesso!")
            self.mostrar_transacoes()

    # ----- Formulário -----
    def abrir_form_nova(self):
        self._form(titulo="Nova Transação", transacao=None)

    def abrir_form_editar(self, transacao):
        self._form(titulo="Editar Transação", transacao=transacao)

    def _form(self, titulo, transacao=None):
        janela = tk.Toplevel(self)
        janela.title(titulo)
        janela.geometry("420x380")
        janela.resizable(False, False)
        janela.configure(bg="#f4f6f9")
        janela.grab_set()

        tk.Label(janela, text=titulo, bg="#f4f6f9",
                 font=("Segoe UI", 13, "bold"), fg="#1e293b").pack(pady=(20, 15))

        frame = tk.Frame(janela, bg="#f4f6f9")
        frame.pack(padx=30, fill="x")

        # Tipo
        tk.Label(frame, text="Tipo", bg="#f4f6f9", font=("Segoe UI", 9, "bold"),
                 fg="#64748b").grid(row=0, column=0, sticky="w", pady=(0, 4))
        tipo_var = tk.StringVar(value=transacao.tipo if transacao else "receita")
        tipo_frame = tk.Frame(frame, bg="#f4f6f9")
        tipo_frame.grid(row=1, column=0, sticky="w", pady=(0, 12))
        tk.Radiobutton(tipo_frame, text="✅ Receita", variable=tipo_var, value="receita",
                       bg="#f4f6f9", font=("Segoe UI", 10)).pack(side="left", padx=(0, 10))
        tk.Radiobutton(tipo_frame, text="🔴 Despesa", variable=tipo_var, value="despesa",
                       bg="#f4f6f9", font=("Segoe UI", 10)).pack(side="left")

        # Descrição
        tk.Label(frame, text="Descrição", bg="#f4f6f9", font=("Segoe UI", 9, "bold"),
                 fg="#64748b").grid(row=2, column=0, sticky="w", pady=(0, 4))
        descricao_entry = tk.Entry(frame, font=("Segoe UI", 10), width=35)
        descricao_entry.grid(row=3, column=0, sticky="ew", pady=(0, 12))
        if transacao:
            descricao_entry.insert(0, transacao.descricao)

        # Valor
        tk.Label(frame, text="Valor (R$)", bg="#f4f6f9", font=("Segoe UI", 9, "bold"),
                 fg="#64748b").grid(row=4, column=0, sticky="w", pady=(0, 4))
        valor_entry = tk.Entry(frame, font=("Segoe UI", 10), width=35)
        valor_entry.grid(row=5, column=0, sticky="ew", pady=(0, 12))
        if transacao:
            valor_entry.insert(0, str(transacao.valor))

        # Categoria
        tk.Label(frame, text="Categoria", bg="#f4f6f9", font=("Segoe UI", 9, "bold"),
                 fg="#64748b").grid(row=6, column=0, sticky="w", pady=(0, 4))
        categoria_var = tk.StringVar(value=transacao.categoria if transacao else "")
        categoria_combo = ttk.Combobox(frame, textvariable=categoria_var,
                                       values=CATEGORIAS_PADRAO, width=33)
        categoria_combo.grid(row=7, column=0, sticky="ew", pady=(0, 16))

        # Botão salvar
        def salvar():
            erros = []
            try:
                tipo = validar_tipo(tipo_var.get())
            except ValueError as e:
                erros.append(str(e))

            try:
                descricao = validar_descricao(descricao_entry.get())
            except ValueError as e:
                erros.append(str(e))

            try:
                valor = validar_valor(valor_entry.get())
            except ValueError as e:
                erros.append(str(e))

            try:
                categoria = validar_categoria(categoria_var.get())
            except ValueError as e:
                erros.append(str(e))

            if erros:
                messagebox.showerror("Erro de validação", "\n".join(erros))
                return

            if transacao:
                service.editar_transacao(transacao.id, tipo, descricao, valor, categoria)
                messagebox.showinfo("Sucesso", "Transação atualizada!")
            else:
                service.adicionar_transacao(tipo, descricao, valor, categoria)
                messagebox.showinfo("Sucesso", "Transação adicionada!")

            janela.destroy()
            self.mostrar_transacoes()

        tk.Button(janela, text="Salvar transação", bg="#6366f1", fg="white",
                  font=("Segoe UI", 10, "bold"), bd=0, padx=16, pady=8,
                  cursor="hand2", command=salvar).pack(pady=(0, 10))


# --------------------------------------------------

if __name__ == "__main__":
    app = App()
    app.mainloop()