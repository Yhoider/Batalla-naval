import pytest
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


def test_crear_usuario_duplicado(capfd):
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario1", "password123")
    
    sistema.crear_cuenta("usuario1", "nuevopassword")
    
    captured = capfd.readouterr()
    assert "El usuario ya existe." in captured.out


def test_iniciar_sesion_con_contrasena_incorrecta(capfd):
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    
    usuario = sistema.iniciar_sesion("usuario2", "wrongpassword")
    
    captured = capfd.readouterr()
    
    assert usuario is None
    assert "Credenciales incorrectas." in captured.out