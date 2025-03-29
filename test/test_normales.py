import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tc.campo import Campo
from src.tc.juego import juego
from src.tc.SistemaUsuarios import SistemaUsuarios


def test_generar_campo():
    campo = Campo(5,5)
    matriz = campo.generar_campo()
    assert len(matriz) == 5

def test_generar_campo():
    campo = Campo(10,6)
    matriz = campo.generar_campo()
    assert len(matriz) == 10

def test_generar_campo():
    campo = Campo(100,100)
    matriz = campo.generar_campo()
    assert len(matriz) == 100


@pytest.fixture
def sistema():
    return SistemaUsuarios()

@pytest.fixture
def juego_fixture():
    return juego(5, "usuario_test")

def test_crear_cuenta(sistema):
    sistema.crear_cuenta("usuario1", "contraseña")
    assert "usuario1" in sistema.usuarios

def test_crear_cuenta_nueva(sistema):
    sistema.crear_cuenta("usuario2", "contraseña")
    assert "usuario2" in sistema.usuarios

def test_crear_cuenta_dos_veces(sistema):
    sistema.crear_cuenta("usuario3", "contraseña")
    sistema.crear_cuenta("usuario3", "otra_contraseña")
    assert "El usuario ya existe." 

def test_iniciar_sesion_exitoso(sistema):
    sistema.crear_cuenta("usuario4", "contraseña")
    usuario = sistema.iniciar_sesion("usuario4", "contraseña")
    assert usuario is not None

def test_iniciar_sesion_incorrecto(sistema):
    sistema.crear_cuenta("usuario5", "contraseña")
    usuario = sistema.iniciar_sesion("usuario5", "contraseña_incorrecta")
    assert usuario is None

def test_iniciar_sesion_usuario_no_existente(sistema):
    usuario = sistema.iniciar_sesion("usuario_no_existente", "contraseña")
    assert usuario is None

def test_cambiar_password(sistema):
    sistema.crear_cuenta("usuario6", "contraseña")
    sistema.cambiar_password("usuario6", "nueva_contraseña")
    usuario = sistema.iniciar_sesion("usuario6", "nueva_contraseña")
    assert usuario is not None

def test_cambiar_password_misma_contraseña(sistema):
    sistema.crear_cuenta("usuario7", "contraseña")
    sistema.cambiar_password("usuario7", "contraseña")
    usuario = sistema.iniciar_sesion("usuario7", "contraseña")
    assert usuario is not None

def test_cambiar_password_usuario_no_existente(sistema):
    sistema.cambiar_password("usuario_no_existente", "nueva_contraseña")
    assert "Usuario no encontrado." 

def test_disparar_acierto(juego_fixture):
    juego_fixture.campo.matriz = [["🚤"]]
    juego_fixture.disparar()
    assert juego_fixture.puntaje == 1

def test_disparar_fallo(juego_fixture):
    juego_fixture.campo.matriz = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    juego_fixture.disparar()
    assert juego_fixture.puntaje == 0

def test_disparar_varias_veces(juego_fixture):
    juego_fixture.campo.matriz = [["🚤", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    juego_fixture.disparar()
    juego_fixture.disparar()
    assert juego_fixture.puntaje <= 1