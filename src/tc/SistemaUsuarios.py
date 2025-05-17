from src.tc.Jugador import Jugador

class SistemaUsuarios:
    """
    Gestiona los usuarios del sistema: creación de cuentas, inicio de sesión y cambio de contraseña.
    """
    def __init__(self):
        """
        Inicializa el sistema de usuarios con un diccionario vacío.
        """
        self.usuarios = {}

    def crear_cuenta(self, user: str, password: str):
        """
        Crea una nueva cuenta de usuario.

        :param user: Nombre de usuario.
        :param password: Contraseña deseada.
        """
        if user in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[user] = Jugador(user, password)
            print("Cuenta creada exitosamente.")

    def iniciar_sesion(self, user: str, password: str):
        """
        Inicia sesión de un usuario si las credenciales son correctas.

        :param user: Nombre de usuario.
        :param password: Contraseña.
        :return: Objeto Jugador si la autenticación es exitosa, None en caso contrario.
        """
        usuario = self.usuarios.get(user)
        if usuario is not None and usuario.password == password:
            print(f"Ingreso exitoso. Bienvenido, {user}.")
            return usuario
        else:
            print("Credenciales incorrectas.")
            return None

    def cambiar_password(self, user: str, nueva_password: str):
        """
        Cambia la contraseña de un usuario existente.

        :param user: Nombre de usuario.
        :param nueva_password: Nueva contraseña.
        """
        usuario = self.usuarios.get(user)
        if usuario:
            usuario.password = nueva_password
            print("Contraseña cambiada exitosamente.")
        else:
            print("Usuario no encontrado.")



