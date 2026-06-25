import os
from flask import Flask, render_template, request, redirect, url_for, flash
from database import db
from services.financeiro import FinanceiroService
from utils.validacoes import validar_tipo, validar_valor, validar_descricao, validar_categoria, CATEGORIAS_PADRAO

app = Flask(__name__)

# config
app.config["SECRET_KEY"] = "financeiro-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///financeiro.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

service = FinanceiroService()


@app.before_request
def criar_tabelas():
    """Garante que as tabelas existam antes da primeira requisição."""
    db.create_all()


# ROTAS
@app.route("/")
def index():
    """Dashboard principal com resumo financeiro."""
    receitas, despesas, saldo = service.calcular_saldo()
    transacoes = service.listar_transacoes()[:5]
    resumo_categorias = service.resumo_por_categoria()

    return render_template(
        "index.html",
        receitas=receitas,
        despesas=despesas,
        saldo=saldo,
        transacoes=transacoes,
        resumo_categorias=resumo_categorias,
    )


@app.route("/transacoes")
def listar():
    """Lista todas as transações com filtro opcional por categoria."""
    categoria_filtro = request.args.get("categoria", "").strip().lower()
    categorias = service.listar_categorias()

    if categoria_filtro:
        transacoes = service.filtrar_por_categoria(categoria_filtro)
    else:
        transacoes = service.listar_transacoes()

    return render_template(
        "transacoes.html",
        transacoes=transacoes,
        categorias=categorias,
        categoria_filtro=categoria_filtro,
        categorias_padrao=CATEGORIAS_PADRAO,
    )


@app.route("/transacoes/nova", methods=["GET", "POST"])
def nova_transacao():
    """Formulário e processamento de nova transação."""
    if request.method == "POST":
        erros = []

        try:
            tipo = validar_tipo(request.form.get("tipo", ""))
        except ValueError as e:
            erros.append(str(e))
            tipo = ""

        try:
            descricao = validar_descricao(request.form.get("descricao", ""))
        except ValueError as e:
            erros.append(str(e))
            descricao = ""

        try:
            valor = validar_valor(request.form.get("valor", ""))
        except ValueError as e:
            erros.append(str(e))
            valor = 0

        try:
            categoria = validar_categoria(request.form.get("categoria", ""))
        except ValueError as e:
            erros.append(str(e))
            categoria = ""

        if erros:
            for erro in erros:
                flash(erro, "erro")
            return render_template(
                "form_transacao.html",
                acao="Nova",
                categorias_padrao=CATEGORIAS_PADRAO,
                form=request.form,
            )

        service.adicionar_transacao(tipo, descricao, valor, categoria)
        flash("Transação adicionada com sucesso!", "sucesso")
        return redirect(url_for("listar"))

    return render_template(
        "form_transacao.html",
        acao="Nova",
        categorias_padrao=CATEGORIAS_PADRAO,
        form={},
    )


@app.route("/transacoes/editar/<int:id>", methods=["GET", "POST"])
def editar_transacao(id):
    """Formulário e processamento de edição de transação."""
    transacao = service.buscar_por_id(id)
    if not transacao:
        flash("Transação não encontrada.", "erro")
        return redirect(url_for("listar"))

    if request.method == "POST":
        erros = []

        try:
            tipo = validar_tipo(request.form.get("tipo", ""))
        except ValueError as e:
            erros.append(str(e))
            tipo = transacao.tipo

        try:
            descricao = validar_descricao(request.form.get("descricao", ""))
        except ValueError as e:
            erros.append(str(e))
            descricao = transacao.descricao

        try:
            valor = validar_valor(request.form.get("valor", ""))
        except ValueError as e:
            erros.append(str(e))
            valor = transacao.valor

        try:
            categoria = validar_categoria(request.form.get("categoria", ""))
        except ValueError as e:
            erros.append(str(e))
            categoria = transacao.categoria

        if erros:
            for erro in erros:
                flash(erro, "erro")
            return render_template(
                "form_transacao.html",
                acao="Editar",
                categorias_padrao=CATEGORIAS_PADRAO,
                form=request.form,
                transacao=transacao,
            )

        service.editar_transacao(id, tipo, descricao, valor, categoria)
        flash("Transação atualizada com sucesso!", "sucesso")
        return redirect(url_for("listar"))

    return render_template(
        "form_transacao.html",
        acao="Editar",
        categorias_padrao=CATEGORIAS_PADRAO,
        form=transacao.to_dict(),
        transacao=transacao,
    )


@app.route("/transacoes/excluir/<int:id>", methods=["POST"])
def excluir_transacao(id):
    """Exclui uma transação pelo id."""
    excluido = service.excluir_transacao(id)
    if excluido:
        flash("Transação excluída.", "sucesso")
    else:
        flash("Transação não encontrada.", "erro")
    return redirect(url_for("listar"))



if __name__ == "__main__":
    app.run(debug=True)