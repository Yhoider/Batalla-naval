import pytest

from src.tc.SistemaUsuarios import SistemaUsuarios
from src.tc.juego import juego
from src.tc.campo import Campo



def test_iniciar_sesion_usuario_no_existente():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario_Inexistente", "password123")  
    usuario = sistema.iniciar_sesion("usuario_inexistente", "password123") 
    assert "Credenciales incorrectas." 


def test_iniciar_sesion_con_contraseña_incorrecta():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    
    usuario = sistema.iniciar_sesion("usuario2", "wrongpassword")

    assert usuario is None
    assert "Credenciales incorrectas." 

def test_crear_cuenta_error_3():
    sistema = SistemaUsuarios()
    assert sistema.crear_cuenta("usuario9", "") is None 


def test_cambio_contraseña ():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    sistema.cambiar_password("hR.WELLS", "password")
    assert "Usuario no encontrado." 