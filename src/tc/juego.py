from src.tc.campo import Campo

class Juego ():
    """
    Clase que controla el flujo del juego de batalla naval.
    """
    def __init__(self, fila:int, columna:int, user:str):
        """
        Inicializa un nuevo juego con dimensiones del campo y el usuario activo.

        :param fila: Número de filas del campo.
        :param columna: Número de columnas del campo.
        :param user: Nombre del jugador.
        """
        self.fila = fila
        self.columna = columna
        self.puntaje = 0
        self.user = user
        self.campo = Campo(self.fila, self.columna)
    
    def iniciar_juego(self):
        """
        Inicia el juego generando un nuevo campo y mostrando su estado inicial.
        """
        self.campo.generar_campo()
        print("Campo generado:", self.campo.matriz)
        
    def disparar(self):
        """
        Permite al jugador atacar posiciones en el campo hasta que se acaben los intentos
        o se destruyan todos los barcos.
        """
        for i in range (0,(len(self.campo.matriz)*self.columna), 1):
            fila = int(input("Introduce la coordenada del barco a atacar (fila): ")) - 1 
            columna = int(input("Introduce la coordenada del barco a atacar (columna): ")) - 1

            if 0 <= fila <= self.fila and 0 <= columna <= self.columna:
                if self.campo.matriz[fila][columna] == "🚤" or self.campo.matriz[fila][columna] == "🛥️":
                    self.campo.matriz[fila][columna] = "_"
                    self.puntaje += 1
                else:
                    print("Fallaste. Intenta de nuevo.")
            else:
                print("Coordenadas fuera del campo.")

            if not any("🚤" in fila or "🛥️" in fila for fila in self.campo.matriz):
                print("¡Todos los barcos han sido hundidos! Fin del juego.")
                break
            
        print ("Juegos terminado.")
        tabla = (f"user:{self.user}  puntaje: {self.puntaje}")
        print (tabla)    


            
