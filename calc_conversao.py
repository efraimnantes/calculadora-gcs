# calc_conversao.py
# Módulo E - Conversão
# Autor: Pedro Henrique Mendes
# Branch: feature/modulo-conversao

def celsius_para_fahrenheit(celsius):
    """Converte Celsius para Fahrenheit.
    Lança ValueError se a temperatura for inferior ao zero absoluto (-273.15°C)."""
    if celsius < -273.15:
        raise ValueError("A temperatura não pode ser inferior ao zero absoluto (-273.15°C).")
    return (celsius * 9 / 5) + 32

def km_para_milhas(km):
    """Converte quilômetros para milhas.
    Lança ValueError se a distância for negativa."""
    if km < 0:
        raise ValueError("A distância em quilômetros não pode ser negativa.")
    return km * 0.621371

def kg_para_libras(kg):
    """Converte quilogramas para libras.
    Lança ValueError se a massa for negativa."""
    if kg < 0:
        raise ValueError("A massa em quilogramas não pode ser negativa.")
    return kg * 2.20462
