from src.tc.campo import Campo

class juego ():
    def __init__(self,numero:int, user:str):
        self.numero = numero
        self.puntaje = 0
        self.user = user
        self.campo = Campo(self.numero)
    
    def iniciar_juego(self):
        self.campo.generar_campo()
        print("Campo generado:\n", self.campo.matriz)
        
    def disparar(self):
        for i in range (self.numero):
            fila = int(input("Introduce la coordenada del barco a atacar (fila): ")) - 1 
            columna = int(input("Introduce la coordenada del barco a atacar (columna): ")) - 1
            
            if self.campo.matriz[fila][columna] == "🚤" or self.campo.matriz[fila][columna] == "🛥️":
                self.campo.matriz[fila][columna] = "_"
                self.puntaje += 1
            else:
                print("Fallaste. Intenta de nuevo.")
        print ("Juegos terminado.")
        tabla = (f"user:{self.user}:puntaje: {self.puntaje}")
        print (tabla)    
            