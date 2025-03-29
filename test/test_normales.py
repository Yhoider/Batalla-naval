import pytest
from unittest.mock import patch
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

def test_campo_generacion():
    campo = Campo(5, 5)
    matriz = campo.generar_campo()
    assert len(matriz) == 5
    assert all(len(fila) == 5 for fila in matriz)
    assert all(celda in ["_", "🚤", "🛥️"] for fila in matriz for celda in fila)

def test_juego_inicializacion():
    partida = juego(3, 3, "Player1")
    assert partida.fila == 3
    assert partida.columna == 3
    assert partida.puntaje == 0
    assert partida.user == "Player1"
    

def test_juego_iniciar():
    partida = juego(4, 4, "TestUser")
    partida.iniciar_juego()
    assert len(partida.campo.matriz) == 4
    assert all(len(fila) == 4 for fila in partida.campo.matriz)

def test_juego_disparo_acierto(monkeypatch):
    partida = juego(3, 3, "Player2")
    partida.campo.matriz = [["🚤", "_", "_"],
                             ["_", "_", "_"],
                             ["_", "_", "_"]]
    
    inputs = iter([1, 1])  # Disparo a (0,0)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    partida.disparar()
    assert partida.puntaje == 1
    assert partida.campo.matriz[0][0] == "_"

def test_juego_disparo_fallo(monkeypatch):
    partida = juego(3, 3, "Player3")
    partida.campo.matriz = [["_", "_", "_"],
                             ["_", "_", "_"],
                             ["_", "_", "_"]]
    
    inputs = iter([1, 1])  # Disparo a (0,0)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    partida.disparar()
    assert partida.puntaje == 0
    assert partida.campo.matriz[0][0] == "_"


def test_juego_todos_hundidos(monkeypatch, capsys):
    partida = juego(2, 2, "Player5")
    partida.campo.matriz = [["🚤", "🛥️"],
                             ["🚤", "🛥️"]]
    
    inputs = iter([1, 1, 1, 2, 2, 1, 2, 2])  # Disparos en todas las posiciones
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    partida.disparar()
    captured = capsys.readouterr()
    assert "¡Todos los barcos han sido hundidos! Fin del juego." in captured.out
