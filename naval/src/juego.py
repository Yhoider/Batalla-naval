from campo import campo
from jugador import jugador 

class juego (jugador):
    def __init__(self,numero:int):
        self.numero = numero
        self.puntaje = 0
        self.matriz = campo.matriz 
    
    def inicializar_campo (self):
        self.Campo = campo(self.numero)
        self.generar_campo = self.Campo.generar_campo ()
        
    def disparar(self):
        for i in range (self.numero):
            fila = (int(input("Intoduce la coordenada del barco a atarcar (fila:)"))) - 1 
            columna = (int(input("Intoduce la coordenada del barco a atarcar (columna:)"))) - 1
            if self.Campo.matriz == "🚤" or self.Campo.matriz[fila][columna]== "🛥️":
                self.Campo.matriz [fila] [columna] = "_"
                self.puntaje += 1
    
    def tabla_puntaje (self) -> dict:
        tabla = {
            'user': self.user,
            'puntaje': self.puntaje
        }
        return tabla    
            
prueba = juego (7)
prueba.inicializar_campo ()
prueba.disparar()