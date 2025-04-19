from src.tc.Jugador import Jugador

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, user: str, password: str):
        if user in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[user] = Jugador(user, password)
            print("Cuenta creada exitosamente.")

    def iniciar_sesion(self, user: str, password: str):
        usuario = self.usuarios.get(user)
        if usuario is not None and usuario.password == password:
            print(f"Ingreso exitoso. Bienvenido, {user}.")
            return usuario
        else:
            print("Credenciales incorrectas.")
            return None

    def cambiar_password(self, user: str, nueva_password: str):
        usuario = self.usuarios.get(user)
        if usuario:
            usuario.password = nueva_password
            print("Contraseña cambiada exitosamente.")
        else:
            print("Usuario no encontrado.")



