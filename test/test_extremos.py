import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tc.campo import Campo


def test_campo_minimo():
    campo = Campo(1)
    matriz = campo.generar_campo()
    assert len(matriz) == 1
    assert len(matriz[0]) == 1


def test_campo_maximo():
    campo = Campo(1000)
    matriz = campo.generar_campo()
    assert len(matriz) == 1000


def test_campo_tamano_cero():
    campo = Campo(0)
    matriz = campo.generar_campo()
    
    assert matriz == []