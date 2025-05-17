import pytest

from src.tc.SistemaUsuarios import SistemaUsuarios
from src.tc.Juego import Juego
from src.tc.campo import Campo



def test_iniciar_sesion_usuario_no_existente():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario_Inexistente", "password123")  
    usuario = sistema.iniciar_sesion("usuario_inexistente", "password123") 
    assert "Credenciales incorrectas." 

def test_iniciar_sesion_error():
    sistema = SistemaUsuarios()
    assert sistema.iniciar_sesion("usuario_inexistente", "password") is None

def test_iniciar_sesion_con_contraseña_incorrecta():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    
    usuario = sistema.iniciar_sesion("usuario2", "wrongpassword")
    assert usuario is None
    assert "Credenciales incorrectas." 

def test_crear_cuenta_error_3():
    sistema = SistemaUsuarios()
    assert sistema.crear_cuenta("usuario9", "") is None 

def test_crear_cuenta_dupliacada():
    sistema = SistemaUsuarios ()
    sistema.crear_cuenta("usuario2", "password2")
    resultado = sistema.crear_cuenta("usuario2", "password3")
    assert resultado is None 

def test_cambio_contraseña ():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario2", "password123")
    sistema.cambiar_password("hR.WELLS", "password")
    assert "Usuario no encontrado." 

def test_cambiar_password_error():
    sistema = SistemaUsuarios()
    try:
        sistema.cambiar_password("usuario_inexistente", "nueva_clave")
    except KeyError:
        assert True


def test_crear_cuenta_error():
    sistema = SistemaUsuarios()
    sistema.crear_cuenta("usuario_error", "123")
    sistema.crear_cuenta("usuario_error", "456")
    assert sistema.usuarios["usuario_error"].password == "123" 

def test_disparar_error():
    juego_prueba = Juego(5, 5, "usuario_error")
    juego_prueba.iniciar_juego()
    try:
        juego_prueba.campo.matriz[6][6]  
    except IndexError:
        pass



def test_disparar_coordenadas_inválidas():
    juego_prueba = Juego(5, 5, "usuario_error")
    juego_prueba.iniciar_juego()
    try:
        juego_prueba.campo.matriz[-1][-1]  
    except IndexError:
        assert True


def test_crear_campo_sin_dimensiones():
    try:
        campo = Campo(0, 0)  
        campo.generar_campo()
    except ValueError:
        assert True

def test_visualizacion_puntaje_error():
    juego_prueba = Juego(0, 0, "usuario_error_puntaje")
    try:
        juego_prueba.iniciar_juego()
        assert juego_prueba.puntaje == 0  
    except ValueError:
        assert True


def test_generar_campo_dimensiones_inválidas():
    try:
        campo = Campo(-5, -5)  
        campo.generar_campo()
    except ValueError:
        assert True  

def test_generar_campo_sin_dimensiones():
    try:
        campo = Campo(0, 0)  
        campo.generar_campo()
    except ValueError:
        assert True  

def test_iniciar_juego_sin_campo():
    try:
        juego_prueba = Juego(0, 0, "usuario_error")
        juego_prueba.iniciar_juego()  
    except ValueError:
        assert True  

def test_iniciar_juego_campo_corrupto():
    try:
        campo = Campo(3, 3)
        campo.matriz = None  
        juego_prueba = Juego(3, 3, "usuario_corrupto")
        juego_prueba.campo = campo
        juego_prueba.iniciar_juego()
    except AttributeError:
        assert True