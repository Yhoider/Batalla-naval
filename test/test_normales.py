import pytest
from src.tc.campo import Campo
from src.tc.juego import juego
from src.tc.SistemaUsuarios import SistemaUsuarios

def test_generar_campo():
    campo = Campo(5)
    matriz = campo.generar_campo()
    assert len(matriz) == 5
    assert all(len(fila) == 5 for fila in matriz)


def test_crear_y_iniciar_sesion_usuario():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario4", "password456")
    
    usuario = sistema.iniciar_sesion("usuario4", "password456")
    
    assert usuario is not None  
    assert usuario.user == "usuario4" 

def test_cambiar_contrasena_usuario():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario5", "password789")
    
    sistema.cambiar_contrasena("usuario5", "nuevapassword")
    usuario = sistema.iniciar_sesion("usuario5", "nuevapassword")
    
    assert usuario is not None  
    assert usuario.password == "nuevapassword"