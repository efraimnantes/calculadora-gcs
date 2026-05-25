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