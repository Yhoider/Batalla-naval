import random as rd

class campo:
    def __init__(self, numero:int):
        self.numero = numero
        self.matriz:list[list] = []
        self.nave:list = ["_","🚤", "🛥️"]

    def generar_campo (self) -> list[list[str]]:
        for i in range(self.numero):
            self.fila:list = []
            for j in range (self.numero):
                self.fila.append(rd.choice(self.nave))
            self.matriz.append(self.fila)   
        return self.matriz                                                               
    
    
    

prueba = campo(5)
prueba.generar_campo()
print(prueba.matriz)