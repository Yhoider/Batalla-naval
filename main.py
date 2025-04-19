from src.tc.campo import Campo
from src.tc.Jugador import Jugador
from src.tc.Juego import Juego
from src.tc.SistemaUsuarios import SistemaUsuarios


if __name__ == "__main__":

    user = input("Crear usuario: ")
    password = input("Crear contraseña: ")
    sistema_usuarios = SistemaUsuarios()
    sistema_usuarios.crear_cuenta(user, password)
    cambio = str(input("¿Quieres cambiar tu Contraseña? (si o no)")).lower ()
    if cambio == "si":
        new_password = str(input("Ingresa tu nueva contraseña:"))
        sistema_usuarios.cambiar_password(user,new_password)

    while True:
        confirmar_user = input("Nombre de usuario: ")
        confirmar_password = input("Contraseña: ")

        usuario = sistema_usuarios.iniciar_sesion(confirmar_user, confirmar_password)

        if usuario:
            fila = int(input("Ingresa el numero de filas del campo:"))
            columna = int(input("Inresa el nuemro de columna del campo:"))
            juego = Juego(fila, columna, user)  
            juego.user = usuario
            juego.iniciar_juego()
            juego.disparar()
            break  
        else:
            print("Por favor, intenta de nuevo.")