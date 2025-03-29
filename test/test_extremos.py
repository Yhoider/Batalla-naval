import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tc.campo import Campo
from src.tc.SistemaUsuarios import SistemaUsuarios
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


def test_campo_tamano_cero():
    campo = Campo(0)
    matriz = campo.generar_campo()
    
    assert matriz == []


@pytest.fixture
def sistema():
    return SistemaUsuarios()

def test_crear_cuenta_extremo_1(sistema):
    sistema.crear_cuenta("u", "p")
    assert "u" in sistema.usuarios

def test_crear_cuenta_extremo_2(sistema):
    sistema.crear_cuenta("usuario_extremo_largo_12345", "contraseña")
    assert "usuario_extremo_largo_12345" in sistema.usuarios

def test_crear_cuenta_extremo_3(sistema):
    sistema.crear_cuenta("usuario6", "c")
    assert "usuario6" in sistema.usuarios

def test_iniciar_sesion_extremo_1(sistema):
    sistema.crear_cuenta("a", "b")
    assert sistema.iniciar_sesion("a", "b") is not None

def test_cambiar_password_extremo_1(sistema):
    sistema.crear_cuenta("usuario7", "contraseña")
    sistema.cambiar_password("usuario7", "nueva")
    assert sistema.iniciar_sesion("usuario7", "nueva") is not None


def test_crear_cuenta_extremo_2(sistema):
    sistema.crear_cuenta("usuario_extremo_largo_12345", "contraseña")
    assert "usuario_extremo_largo_12345" in sistema.usuarios

def test_crear_cuenta_extremo_3(sistema):
    sistema.crear_cuenta("usuario6", "c")
    assert "usuario6" in sistema.usuarios


@pytest.fixture
def juego_extremo():
    return juego(1, "usuario_extremo")

def test_iniciar_juego_extremo(juego_extremo):
    juego_extremo.iniciar_juego()
    assert len(juego_extremo.campo.matriz) == 1

def test_disparar_extremo(juego_extremo, monkeypatch):
    juego_extremo.iniciar_juego()
    
    monkeypatch.setattr('builtins.input', lambda _: '1')
    
    juego_extremo.disparar()
    assert juego_extremo.puntaje >= 0