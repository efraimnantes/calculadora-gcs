# calc_percentual.py
# Módulo C - Percentual
# Autor: Seu Nome (ou o nome do colega responsável)
# Branch: feature/modulo-percentual

def percentual(valor, porcentagem):
    """Calcula o valor correspondente à percentagem de um dado valor.
    Lança ValueError se o valor ou a percentagem forem negativos."""
    if porcentagem < 0:
        raise ValueError("A percentagem não pode ser negativa.")
    if valor < 0:
        raise ValueError("O valor base não pode ser negativo.")
    return valor * (porcentagem / 100)

def acrescimo(valor, porcentagem):
    """Adiciona uma percentagem a um valor existente."""
    # O tratamento de valores negativos é herdado da função percentual()
    return valor + percentual(valor, porcentagem)

def desconto(valor, porcentagem):
    """Subtrai uma percentagem de um valor existente.
    Lança ValueError se a percentagem de desconto for maior que 100%."""
    if porcentagem > 100:
        raise ValueError("A percentagem de desconto não pode ser superior a 100%.")
    
    # O restante tratamento de valores negativos é herdado da função percentual()
    return valor - percentual(valor, porcentagem)
