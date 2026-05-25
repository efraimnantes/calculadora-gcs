# calc_percentual.py
# Módulo C - Percentual

def percentual(valor, porcentagem):
    """Calcula quanto é a porcentagem de um valor."""
    return valor * (porcentagem / 100)

def acrescimo(valor, porcentagem):
    """Acrescenta a porcentagem ao valor original."""
    return valor + percentual(valor, porcentagem)

def desconto(valor, porcentagem):
    """Desconta a porcentagem do valor original."""
    return valor - percentual(valor, porcentagem)
