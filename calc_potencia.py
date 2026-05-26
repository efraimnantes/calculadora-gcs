# calc_potencia.py
# Módulo B - Potência

def potencia(base, expoente):
    """Retorna a base elevada ao expoente."""
    return base ** expoente

def raiz_quadrada(numero):
    """Retorna a raiz quadrada do número. Lança ValueError se for negativo."""
    if numero < 0:
        raise ValueError("Não é possível calcular a raiz quadrada de um número negativo no conjunto dos reais.")
    return numero ** 0.5

def raiz_cubica(numero):
    """Retorna a raiz cúbica do número."""
    if numero < 0:
        return -(-numero) ** (1.0 / 3.0)
    return numero ** (1.0 / 3.0)
