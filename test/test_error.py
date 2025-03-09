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
    usuario = sistema.iniciar_sesion("usuario_inexistente", "password123") 
    captured = capfd.readouterr()
    assert usuario is None
    assert "Credenciales incorrectas." in captured.out


def test_iniciar_sesion_con_contrasena_incorrecta():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    
    usuario = sistema.iniciar_sesion("usuario2", "wrongpassword")

    assert usuario is None
    assert "Credenciales incorrectas." 

