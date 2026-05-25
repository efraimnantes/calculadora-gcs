def menu():
    print("=== Calculadora GCS ===\n")

    try:
        from calc_basico import somar, subtrair, multiplicar, dividir
        print("Módulo Básico carregado.")
        print("2 + 3 =", somar(2, 3))
    except ImportError:
        print("Módulo Básico ainda não disponível.")

    try:
        from calc_potencia import potencia, raiz_quadrada, raiz_cubica
        print("Módulo Potência carregado.")
        print("2^10 =", potencia(2, 10))
    except ImportError:
        print("Módulo Potência ainda não disponível.")

    try:
        from calc_percentual import percentual, acrescimo, desconto
        print("Módulo Percentual carregado.")
        print("10% de 200 =", percentual(200, 10))
    except ImportError:
        print("Módulo Percentual ainda não disponível.")

    try:
        from calc_estatistica import media, mediana, desvio_padrao
        print("Módulo Estatística carregado.")
        print("Média de [1, 2, 3] =", media([1, 2, 3]))
    except ImportError:
        print("Módulo Estatística ainda não disponível.")

    try:
        from calc_conversao import celsius_para_fahrenheit, km_para_milhas, kg_para_libras
        print("Módulo Conversão carregado.")
        print("30°C em Fahrenheit =", celsius_para_fahrenheit(30))
    except ImportError:
        print("Módulo Conversão ainda não disponível.")


if __name__ == "__main__":
    menu()