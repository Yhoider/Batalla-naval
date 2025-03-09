from campo import Campo

class juego ():
    def __init__(self,numero:int):
        self.numero = numero
        self.puntaje = 0
        self.user = " "
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
                print("¡Tiro exitoso! Puntaje actual:", self.puntaje)
            else:
                print("Fallaste. Intenta de nuevo.")
    
    def tabla_puntaje (self) -> dict:
        tabla = {
            'user': self.user,
            'puntaje': self.puntaje
        }
        return tabla    
            
if __name__ == "__main__":
    Juego = juego(5) 
    Juego.iniciar_juego()
    Juego.disparar()