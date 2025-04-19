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

class SistemaUsuarios:
    def __init__(self):
        self.usuarios = {}

    def crear_cuenta(self, user: str, password: str):
        if user in self.usuarios:
            return False
        else:
            self.usuarios[user] = Jugador(user, password)
            return True

    def iniciar_sesion(self, user: str, password: str):
        usuario = self.usuarios.get(user)
        if usuario is not None and usuario.password == password:
            return usuario
        return None

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Batalla Naval")
        self.geometry("600x500")

        self.sistema_usuarios = SistemaUsuarios()
        self.tab_control = ttk.Notebook(self)

        self.tab_crear_cuenta = ttk.Frame(self.tab_control)
        self.tab_iniciar_sesion = ttk.Frame(self.tab_control)
        self.tab_jugar = ttk.Frame(self.tab_control)

        self.tab_control.add(self.tab_crear_cuenta, text='Crear Cuenta')
        self.tab_control.add(self.tab_iniciar_sesion, text='Iniciar Sesión')
        self.tab_control.add(self.tab_jugar, text='Jugar')

        self.tab_control.pack(expand=1, fill='both')

        self.crear_cuenta_ui()
        self.iniciar_sesion_ui()
        self.jugar_ui()

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
                    messagebox.showinfo("Éxito", "¡Barco hundido!")
                else:
                    messagebox.showinfo("Fallaste", "No hay barco en esa coordenada.")
            else:
                messagebox.showerror("Error", "Coordenadas fuera del campo.")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")

        self.puntaje_label.config(text=f"Puntaje: {self.puntaje}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
