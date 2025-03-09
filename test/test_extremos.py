import pytest
from src.tc.campo import Campo
from src.tc.SistemaUsuarios import SistemaUsuarios
from src.tc.jugador import jugador
from src.tc.juego import juego

def test_campo_minimo():
    campo = Campo(1)
    matriz = campo.generar_campo()
    assert len(matriz) == 1
    assert len(matriz[0]) == 1


def test_campo_maximo():
    campo = Campo(1000)
    matriz = campo.generar_campo()
    assert len(matriz) == 1000
    assert all(len(fila) == 1000 for fila in matriz)

def test_campo_tamano_cero():
    campo = Campo(0)
    matriz = campo.generar_campo()
    
    assert matriz == []