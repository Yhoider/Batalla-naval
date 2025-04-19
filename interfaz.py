import tkinter as tk
from tkinter import ttk, messagebox
import random as rd

class Campo:
    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.matriz = []
        self.nave = ["_", "🚤", "🛥️"]

    def generar_campo(self) -> list[list[str]]:
        self.matriz = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                fila.append(rd.choice(self.nave))
            self.matriz.append(fila)
        return self.matriz

class Jugador:
    def __init__(self, user: str, password: str):
        self.user = user
        self.password = password
        self.max_puntuacion = 0
        self.cuenta_creada = False

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, user: str, password: str):
        if user in self.usuarios:
            return False
        else:
            self.usuarios[user] = Jugador(user, password)
            self.usuarios[user].cuenta_creada = True
            return True

    def iniciar_sesion(self, user: str, password: str):
        usuario = self.usuarios.get(user)
        if usuario is not None and usuario.password == password:
            usuario.max_puntuacion = 0  # Restablecer el contador al iniciar sesión
            return usuario
        return None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Batalla Naval")
        self.geometry("800x600")

        self.sistema_usuarios = SistemaUsuarios()
        self.tab_control = ttk.Notebook(self)

        self.tab_crear_cuenta = ttk.Frame(self.tab_control)
        self.tab_iniciar_sesion = ttk.Frame(self.tab_control)
        self.tab_jugar = ttk.Frame(self.tab_control)
        self.tab_usuarios = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_crear_cuenta, text='Crear Cuenta')
        self.tab_control.add(self.tab_iniciar_sesion, text='Iniciar Sesión')
        self.tab_control.add(self.tab_jugar, text='Jugar')
        self.tab_control.add(self.tab_usuarios, text='Usuarios')

        self.tab_control.pack(expand=1, fill='both')

        self.crear_cuenta_ui()
        self.iniciar_sesion_ui()
        self.jugar_ui()
        self.usuarios_ui()

    def crear_cuenta_ui(self):
        tk.Label(self.tab_crear_cuenta, text="Usuario:").pack(pady=5)
        self.usuario_entry = tk.Entry(self.tab_crear_cuenta)
        self.usuario_entry.pack(pady=5)

        tk.Label(self.tab_crear_cuenta, text="Contraseña:").pack(pady=5)
        self.contraseña_entry = tk.Entry(self.tab_crear_cuenta, show='*')
        self.contraseña_entry.pack(pady=5)

        tk.Button(self.tab_crear_cuenta, text="Crear", command=self.crear_cuenta).pack(pady=20)

    def iniciar_sesion_ui(self):
        tk.Label(self.tab_iniciar_sesion, text="Usuario:").pack(pady=5)
        self.usuario_entry_login = tk.Entry(self.tab_iniciar_sesion)
        self.usuario_entry_login.pack(pady=5)

        tk.Label(self.tab_iniciar_sesion, text="Contraseña:").pack(pady=5)
        self.contraseña_entry_login = tk.Entry(self.tab_iniciar_sesion, show='*')
        self.contraseña_entry_login.pack(pady=5)

        tk.Button(self.tab_iniciar_sesion, text="Iniciar", command=self.iniciar_sesion).pack(pady=20)

    def jugar_ui(self):
        tk.Label(self.tab_jugar, text="Coordenadas:").pack(pady=5)
        tk.Label(self.tab_jugar, text="Fila:").pack(pady=5)
        self.fila_entry = tk.Entry(self.tab_jugar)
        self.fila_entry.pack(pady=5)

        tk.Label(self.tab_jugar, text="Columna:").pack(pady=5)
        self.columna_entry = tk.Entry(self.tab_jugar)
        self.columna_entry.pack(pady=5)

        tk.Button(self.tab_jugar, text="Disparar", command=self.disparar).pack(pady=20)
        self.puntaje_label = tk.Label(self.tab_jugar, text="Puntaje: 0")
        self.puntaje_label.pack(pady=5)

        self.puntaje = 0
        self.campo = None

    def usuarios_ui(self):
        self.usuarios_listbox = tk.Listbox(self.tab_usuarios, width=50)
        self.usuarios_listbox.pack(pady=20)

        tk.Button(self.tab_usuarios, text="Actualizar", command=self.actualizar_usuarios).pack(pady=10)

    def crear_cuenta(self):
        user = self.usuario_entry.get()
        password = self.contraseña_entry.get()

        if self.sistema_usuarios.crear_cuenta(user, password):
            messagebox.showinfo("Éxito", "Cuenta creada exitosamente.")
            self.usuario_entry.delete(0, tk.END)
            self.contraseña_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "El usuario ya existe.")

    def iniciar_sesion(self):
        user = self.usuario_entry_login.get()
        password = self.contraseña_entry_login.get()
        usuario = self.sistema_usuarios.iniciar_sesion(user, password)

        if usuario:
            messagebox.showinfo("Éxito", f"Ingreso exitoso. Bienvenido, {user}.")
            self.fila_entry.delete(0, tk.END)
            self.columna_entry.delete(0, tk.END)
            self.campo = Campo(5, 5)  # Puedes ajustar el tamaño del campo
            self.campo.generar_campo()
            self.puntaje = 0  # Restablecer el contador al iniciar sesión
            self.puntaje_label.config(text=f"Puntaje: {self.puntaje}")
            self.tab_control.select(self.tab_jugar)
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def disparar(self):
        if self.campo is None:
            messagebox.showwarning("Advertencia", "Primero inicia sesión.")
            return

        try:
            fila = int(self.fila_entry.get()) - 1
            columna = int(self.columna_entry.get()) - 1

            if 0 <= fila < self.campo.filas and 0 <= columna < self.campo.columnas:
                if self.campo.matriz[fila][columna] in ["🚤", "🛥️"]:
                    self.campo.matriz[fila][columna] = "_"
                    self.puntaje += 1
                    self.sistema_usuarios.usuarios[self.usuario_entry_login.get()].max_puntuacion = max(
                        self.sistema_usuarios.usuarios[self.usuario_entry_login.get()].max_puntuacion, self.puntaje
                    )
                    messagebox.showinfo("Éxito", "¡Barco hundido!")
                else:
                    messagebox.showinfo("Fallaste", "No hay barco en esa coordenada.")
            else:
                messagebox.showerror("Error", "Coordenadas fuera del campo.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

        self.puntaje_label.config(text=f"Puntaje: {self.puntaje}")

    def actualizar_usuarios(self):
        self.usuarios_listbox.delete(0, tk.END)
        for usuario in self.sistema_usuarios.usuarios.values():
            if usuario.cuenta_creada:
                self.usuarios_listbox.insert(tk.END, f"{usuario.user} - Máxima puntuación: {usuario.max_puntuacion}")
            else:
                self.usuarios_listbox.insert(tk.END, f"{usuario.user} - Máxima puntuación: 0")

if __name__ == "__main__":
    app = App()
    app.mainloop()
