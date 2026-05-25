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
