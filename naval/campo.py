import random as rd

class campo:
    def __init__(self, numero:int = 5):
        self.numero = numero
        self.matriz:list[list] = []
        self.nave:list = ["_", "🚤", "🛥️"]

    def generar_campo (self) -> list[list[str]]:
        for i in range(self.numero):
            self.fila:list = []
            for j in range (self.numero):
                self.fila.append(rd.choice (self.nave))
            self.matriz.append(self.fila)                                                                   
        return self.matriz
    
    def imprimir_campo(self):
        for fila in self.matriz:
            print(" ".join(fila))


prueba = campo ()
prueba.generar_campo()
prueba.imprimir_campo()
