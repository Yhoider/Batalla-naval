from src.tc.campo import Campo
from src.tc.jugador import jugador
from src.tc.juego import juego
from src.tc.SistemaUsuarios import SistemaUsuarios


if __name__ == "__main__":

    sistema_usuarios = SistemaUsuarios()
    sistema_usuarios.crear_cuenta("Hr.wells", "password")

    while True:
        user_input = input("Nombre de usuario: ")
        password_input = input("Contraseña: ")
        usuario = sistema_usuarios.iniciar_sesion(user_input, password_input)

        if usuario:
            Juego = juego(5)  
            Juego.user = usuario
            Juego.iniciar_juego()
            Juego.disparar()
            break  
        else:
            print("Por favor, intenta de nuevo.")