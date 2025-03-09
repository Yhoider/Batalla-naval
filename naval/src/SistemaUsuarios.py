from jugador import jugador

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, user: str, password: str):
        if user in self.usuarios:
            print("El usuario ya existe.")
        else:
            self.usuarios[user] = jugador(user, password)
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


prueba = SistemaUsuarios ()
prueba.crear_cuenta("Hr.wells", "Camilo4515.")
prueba.iniciar_sesion("Hr.wells","Camilo4515.")
prueba.cambiar_password("Hr.wells","HR.WELLS")

