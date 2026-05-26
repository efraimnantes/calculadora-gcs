import pytest

from calc_basico import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(10, 4) == 6


def test_multiplicar():
    assert multiplicar(3, 4) == 12


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)

from calc_potencia import (
    potencia,
    raiz_quadrada,
    raiz_cubica
)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(2, -1) == 0.5

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(0) == 0

def test_raiz_quadrada_negativa():
    with pytest.raises(ValueError):
        raiz_quadrada(-4)

def test_raiz_cubica():
    assert raiz_cubica(27) == 3
    assert raiz_cubica(0) == 0
    assert raiz_cubica(-8) == -2

from calc_percentual import (
    percentual,
    acrescimo,
    desconto
)

def test_percentual():
    assert percentual(200, 10) == 20
    assert percentual(50, 0) == 0

def test_percentual_valores_negativos():
    with pytest.raises(ValueError):
        percentual(-100, 10)
    with pytest.raises(ValueError):
        percentual(100, -10)

def test_acrescimo():
    assert acrescimo(100, 15) == 115
    assert acrescimo(50, 100) == 100

def test_desconto():
    assert desconto(100, 20) == 80
    assert desconto(250, 10) == 225

def test_desconto_maior_que_cem():
    with pytest.raises(ValueError):
        desconto(100, 110)

from calc_estatistica import (
    media,
    mediana,
    desvio_padrao
)

import pytest


def test_media():
    assert media([2, 4, 6]) == 4


def test_media_lista_vazia():
    with pytest.raises(ValueError):
        media([])


def test_mediana_impar():
    assert mediana([1, 3, 2]) == 2


def test_mediana_par():
    assert mediana([1, 2, 3, 4]) == 2.5


def test_mediana_lista_vazia():
    with pytest.raises(ValueError):
        mediana([])


def test_desvio_padrao():
    assert round(desvio_padrao([2, 4, 4, 4, 5, 5, 7, 9]), 2) == 2.0


def test_desvio_padrao_lista_vazia():
    with pytest.raises(ValueError):
        desvio_padrao([])

from calc_conversao import (
    celsius_para_fahrenheit,
    km_para_milhas,
    kg_para_libras
)


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32


def test_km_para_milhas():
    assert round(km_para_milhas(10), 2) == 6.21


def test_kg_para_libras():
    assert round(kg_para_libras(5), 2) == 11.02
