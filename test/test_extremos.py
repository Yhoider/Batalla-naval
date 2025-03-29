import pytest

from src.tc.campo import Campo
from src.tc.SistemaUsuarios import SistemaUsuarios
from src.tc.juego import juego

def test_campo_minimo():
    campo = Campo(1,1)
    matriz = campo.generar_campo()
    assert len(matriz) == 1


def test_campo_maximo():
    campo = Campo(1000,1000)
    matriz = campo.generar_campo()
    assert len(matriz) == 1000


def test_campo_tamano_cero():
    campo = Campo(0,0)
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


def test_cambiar_password_extremo_2(sistema):
    sistema.crear_cuenta("usuario7", "contraseña")
    sistema.cambiar_password("usuario7", "nueva")
    assert sistema.iniciar_sesion("usuario7", "nueva") is not None


def test_crear_cuenta_extremo_3(sistema):
    sistema.crear_cuenta("usuario_extremo_largo_12345", "contraseña")
    assert "usuario_extremo_largo_12345" in sistema.usuarios

def test_crear_cuenta_extremo_(sistema):
    sistema.crear_cuenta("usuario6", "c")
    assert "usuario6" in sistema.usuarios


