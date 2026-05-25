# calc_estatistica.py
# Módulo D — Estatística
# Autor: Pedro Henrique Mendes
# Branch: feature/modulo-estatistica

import math

def media(valores):
    """Retorna a média. Lança ValueError se a lista estiver vazia."""
    if len(valores) == 0:
        raise ValueError("A lista não pode estar vazia.")
    return sum(valores) / len(valores)


def mediana(valores):
    """Retorna a mediana. Lança ValueError se a lista estiver vazia."""
    if len(valores) == 0:
        raise ValueError("A lista não pode estar vazia.")

    ordenados = sorted(valores)
    tamanho = len(ordenados)
    meio = tamanho // 2

    if tamanho % 2 == 1:
        return ordenados[meio]

    return (ordenados[meio - 1] + ordenados[meio]) / 2


def desvio_padrao(valores):
    """Retorna o desvio padrão populacional. Lança ValueError se a lista estiver vazia."""
    if len(valores) == 0:
        raise ValueError("A lista não pode estar vazia.")

    m = media(valores)
    variancia = sum((x - m) ** 2 for x in valores) / len(valores)
    return math.sqrt(variancia)
