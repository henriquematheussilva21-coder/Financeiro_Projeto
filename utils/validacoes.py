CATEGORIAS_PADRAO = [
    "alimentação",
    "transporte",
    "moradia",
    "saúde",
    "educação",
    "lazer",
    "salário",
    "freelance",
    "outros",
]


def validar_tipo(tipo):
    """Aceita apenas receita ou despesa."""
    tipo = tipo.strip().lower()

    if (tipo) not in ("receita", "despesa"):
        raise ValueError("Digite apenas 'receita' ou 'despesa'.")
    
    return tipo


def validar_valor(valor_str):
    """Converte o valor digitado para float."""
    valor_str = valor_str.strip()

    # Adicionei isso por ser comum digitar com vírgular no BR
    if "," in valor_str:
        valor_str = valor_str.replace(".", "").replace (",", ".")

    try:
        valor = float(valor_str)
    except ValueError:
        raise ValueError ("Valor inválido. Ex.: 150 ou 150,90")
    
    if valor <= 0:
        raise ValueError("O valor precisa ser maior que zero.")
    
    return valor


def validar_descricao(descricao):
    """Impede descrição vazia e textos exageradamente longos."""
    descricao = descricao.strip()

    if not descricao:
        raise ValueError("A descrição não pode ficar vazia.")
    
    if len(descricao) > 100:
        raise ValueError("A descrição deve ter no máximo 100 caracteres.")
    
    return descricao


def validar_categoria(categoria):
    """Padroniza a categoria para minúsculo."""
    categoria = categoria.strip().lower()

    if not categoria:
        raise ValueError("A categoria não pode ficar vazia.")
    
    return categoria