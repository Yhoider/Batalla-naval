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


def test_cambiar_password_extremo_1(sistema):
    sistema.crear_cuenta("usuario7", "contraseña")
    sistema.cambiar_password("usuario7", "nueva")
    assert sistema.iniciar_sesion("usuario7", "nueva") is not None

def test_cambiar_password_extremo_2(sistema):
    sistema.crear_cuenta("usuario7", "contraseña")
    sistema.cambiar_password("usuario7", "usuario7")
    assert sistema.iniciar_sesion("usuario7", "usuario7") is not None

def test_cambiar_password_extremo_3(sistema):
    sistema.crear_cuenta("usuario", "contraseña")
    sistema.cambiar_password("usuario", ".")
    assert sistema.iniciar_sesion("usuario", ".") is not None

def test_puntaje_extremo():
    juego_prueba = juego(100, 100, "usuario_extremo")
    juego_prueba.iniciar_juego()
    assert juego_prueba.puntaje == 0


def test_iniciar_sesion_usuario_extremadamente_largo():
    
    sistema = SistemaUsuarios()
    usuario_largo = "usuario" * 50  
    password = "password123"
    sistema.crear_cuenta(usuario_largo, password)
    assert sistema.iniciar_sesion(usuario_largo, password) is not None  


def test_iniciar_sesion_muchos_usuarios():
    
    sistema = SistemaUsuarios()
    for i in range(10000):  
        sistema.crear_cuenta(f"usuario_{i}", f"password_{i}")
    assert sistema.iniciar_sesion("usuario_9999", "password_9999")

def iniciar_sesion(sistema):
    usuario = sistema.iniciar_sesion("a" * 100, "b" * 100)
    assert usuario is not None

def test_iniciar_sesion_extremo():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario_extremo"*10, "password"*10)
    assert sistema.iniciar_sesion("usuario_extremo"*10, "password"*10)





