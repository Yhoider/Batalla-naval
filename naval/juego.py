from campo import campo

class juego:
    def __init__(self,numero:int):
        self.numero = numero
    
    def inicializar_campo (self):
        campo(self.numero)
        self.campo = campo.generar_campo
        
    def disparar(self):
        for i in range (self.numero):
            fila = list(int(input("Intoduce la coordenada del barco a atarcar (fila:")))
            columna = list(int(input("Intoduce la coordenada del barco a atarcar (columna:")))
            if self.campo[fila][columna] == "🚤" or self.campo [fila] [columna]== "🛥️":
                self.campo [fila] [columna] = "_"
                self.puntaje += 1
            

