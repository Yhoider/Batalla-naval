import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.tc.SistemaUsuarios import SistemaUsuarios
from src.tc.juego import juego
from src.tc.campo import Campo

def test_disparar_fuera_de_rango():
    campo = Campo(3)
    campo.generar_campo()
    juego_instance = juego(3)
    juego_instance.campo = campo
    
    with pytest.raises(IndexError):
        juego_instance.campo.matriz[5][5]  

def test_iniciar_sesion_usuario_no_existente(capfd):
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario_Inexistente", "password123")  
    usuario = sistema.iniciar_sesion("usuario_inexistente", "password123") 
    assert "Credenciales incorrectas." 


def test_iniciar_sesion_con_contrasena_incorrecta():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    
    usuario = sistema.iniciar_sesion("usuario2", "wrongpassword")

    assert usuario is None
    assert "Credenciales incorrectas." 

def test_crear_cuenta_error_3():
    sistema = SistemaUsuarios()
    assert sistema.crear_cuenta("usuario9", "") is None 

def test_iniciar_juego_error():
    with pytest.raises(ValueError):
        juego(-1, "usuario_error")  

def test_disparar_error(juego_fixture, monkeypatch):
    juego_fixture.iniciar_juego()
    
    monkeypatch.setattr('builtins.input', lambda _: '10')  
    
    with pytest.raises(IndexError):
        juego_fixture.disparar()